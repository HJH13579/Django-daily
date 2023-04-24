from django.urls import path
from . import views

urlpatterns = [
    path('music/', views.music_list, name='music_list'),
    path('music/<int:music_pk>/', views.music_detail, name='music_detail'),
    path('music/<int:music_pk>/review/', views.review_create, name='review_create'),
    path('review/', views.review_list, name='review_list'),
    path('review/<int:review_pk>/', views.review_detail, name='review_detail'),
]