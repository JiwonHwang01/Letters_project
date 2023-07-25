from django.contrib import admin
from django.urls import path, include
from letters import views

urlpatterns = [
    path('letters/', views.index, name='index'),
    path('letters/login/', views.login, name='log_in'),
    path('letters/signup/', views.signup, name='sign_up'),
    path('letters/<str:user_id>/', views.postbox, name='post_box'),
    path('letters/<str:user_id>/mypage/', views.mypage, name='my_page'),
    path('letters/<str:url>/', views.postmail, name='post_mail'),    
    
]
