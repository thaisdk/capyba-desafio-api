from django.contrib import admin
from django.urls import path
from base import views

urlpatterns = [
    path('', views.homeView, name='home'),

    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.registerView, name='register'),

    path('article/<str:pk>', views.articleView, name='article'),
    path('profile/<str:pk>', views.userProfile, name='profile'),
    path('update-profile/', views.updateProfile, name='update-profile'),

    path('create-article/', views.createArticle, name='create-article'),
    path('update-article/<str:pk>', views.updateArticle, name='update-article'),
    path('delete-article/<str:pk>', views.deleteArticle, name='delete-article'),

    path('delete-message/<str:pk>', views.deleteMessage, name='delete-message'),

]
