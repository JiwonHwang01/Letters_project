from django.shortcuts import render, redirect
from letters.models import User, Letter
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'letters/index.html')

def letter(request, letter_id):
    letter = Letter.objects.get(id=letter_id)
    return

def mypage(request):
    all_letters = Letter.objects.all().order_by("-pub_date")
    print(request)
    return render(request, 'letters/my_page.html', {'letter_list':all_letters})

def postmail(request):
    return