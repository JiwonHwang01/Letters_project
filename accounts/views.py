from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from accounts.forms import UserForm
from letters.models import User
import uuid
import base64
import codecs

def generate_random_slug_code(length=12):
    code = None
    while not code or User.objects.filter(lettercase_url=code).exists():
        code = base64.urlsafe_b64encode(
            codecs.encode(uuid.uuid4().bytes, "base64").rstrip()
            ).decode()[:length]
    return code

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            user.lettercase_url = generate_random_slug_code()
            user.save()
            login(request, user)

            return redirect('/letters/')
        else:
            request.session['fail_reason'] = form.errors
            print("/letters/")
    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})