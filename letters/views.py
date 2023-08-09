from django.shortcuts import render
from letters.models import User

def index(request):
    return render(request, 'letters/index.html')

def login(request):
    if request.method == "POST":
        form = NameForm(request.POST)
    else:
        pass

    return render(request, 'letters/login.html')

def signup(request):

    return render(request, 'letters/signup.html')

def postbox(request):
    return

def mypage(request):
    return
def postmail(request):
    return