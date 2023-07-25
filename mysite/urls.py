from django.contrib import admin
from django.urls import path, include
from letters import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("letters/", include("letters.urls")),
    path("accounts/", include("accounts.urls")),
    
]
