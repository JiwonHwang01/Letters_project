from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from accounts.forms import UserForm
import uuid
import base64
import codecs

def generate_random_slug_code(length=12):

    return base64.urlsafe_b64encode(
        codecs.encode(uuid.uuid4().bytes, "base64").rstrip()
    ).decode()[:length]

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user.lettercase_url = form.cleaned_data['lettercase_url'] or generate_random_slug_code()
            user.save()
            # form.save(update_fields=['lettercase_url'])
            user = authenticate(username = username, password = raw_password)
            login(request, user)

            return redirect('/letters/')
        else:
            print(form.errors)
            print("accounts/views/")
    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})