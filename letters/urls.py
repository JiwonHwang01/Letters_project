from django.contrib import admin
from django.urls import path, include
from letters import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('detail/', views.letterdetail, name='letter_detail'),
    path('mypage/', views.mypage, name='my_page'),
    path('letter/<str:hash_id>/', views.letter, name='letter_detail'),
    path('post/', views.post_letter, name='post_letter'),
    path('<str:token>/', views.write_letter, name='write_letter'),
    
]
