from django.shortcuts import render, redirect
from letters.models import User, Letter
from django.contrib.auth import authenticate, login, get_user

def index(request):
    return render(request, 'letters/index.html')

def letter(request, letter_id):
    letter = Letter.objects.get(id=letter_id)
    return

def mypage(request):
    username = get_user(request)
    all_letters = Letter.objects.filter(user=username).order_by("-pub_date")
    print(get_user(request))
    return render(request, 'letters/my_page.html', {'letter_list':all_letters, 'username':get_user(request)})

def postmail(request):
    return