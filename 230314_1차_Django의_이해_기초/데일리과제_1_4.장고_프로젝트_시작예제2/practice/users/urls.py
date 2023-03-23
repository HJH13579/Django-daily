from django.urls import path
from . import views

urlpatterns = [
    path('hw1/', views.hw1),
    path('hw2/', views.hw2),
    path('hw3/', views.hw3),
    path('hw4/', views.hw4),
    path('hw5/', views.hw5),
]