from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from accounts.forms import UserForm
from letters.models import User
from letters.utils import generate_user_slug_code

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            user.lettercase_url = generate_user_slug_code()
            user.save()
            login(request, user)

            return redirect('/letters/')
        else:
            request.session['fail_reason'] = form.errors
            print("/letters/")
    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})