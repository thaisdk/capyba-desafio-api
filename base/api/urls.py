from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes),
    path('articles/',views.getArticles),
    path('article/<str:pk>',views.getArticle),
]