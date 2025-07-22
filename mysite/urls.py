from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_letters(request):
    return redirect('/letters/')

urlpatterns = [
    path("", redirect_to_letters, name="home"),
    path("admin/", admin.site.urls),
    path("letters/", include("letters.urls")),
    path("accounts/", include("accounts.urls")),
]
