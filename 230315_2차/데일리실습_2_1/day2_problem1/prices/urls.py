from django.urls import path
from prices import views

urlpatterns = [
    path('<thing>/<int:cnt>/',views.price),
]
