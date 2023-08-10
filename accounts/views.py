from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from accounts.forms import UserForm
from letters.models import LetterCase
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
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            case = LetterCase(user= user, letter_url = generate_random_slug_code(), letter_count = 0)
            case.save()
            print(case)
            return redirect('/letters/')
        else:
            print(form.errors)
            print("accounts/views/")
    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})
