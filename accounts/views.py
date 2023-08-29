from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from accounts.forms import UserForm
from letters.models import User
import uuid
import base64
import codecs

def generate_random_slug_code(length=12):

    return base64.urlsafe_b64encode(
        codecs.encode(uuid.uuid4().bytes, "base64").rstrip()
    ).decode()[:length]

def signup(request):
    if request.method == "POST":

        # newUser = request.POST.copy()
        # print(request.POST)
        # newUser['lettercaseUrl'] = url
        
        # print(newUser)
        # form = UserForm(newUser)
        
        form = UserForm(request.POST)
        
        # print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # User.objects.get(username=username).update(lettercase_url=url)

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
