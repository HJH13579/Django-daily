from django.urls import path
from fruits import views

urlpatterns = [
    path('', views.fruit),
]
