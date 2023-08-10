from django.shortcuts import render, redirect
from letters.models import User
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'letters/index.html')

def postbox(request):
    return

def mypage(request):
    return
def postmail(request):
    return