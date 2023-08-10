from django.contrib import admin
from django.urls import path, include
from letters import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('login/', views.login, name='log_in'),
    # path('<str:user_id>/', views.postbox, name='post_box'),
    # path('<str:user_id>/mypage/', views.mypage, name='my_page'),
    path('<str:url>/', views.postmail, name='post_mail'),    
    
]
