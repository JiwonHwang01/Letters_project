from django.contrib import admin
from django.urls import path, include
from letters import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('detail/', views.letterdetail, name='letter_detail'),
    path('mypage/', views.mypage, name='my_page'),
     
]
