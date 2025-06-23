from django.urls import path

from . import views

urlpatterns = [
    path('', views.studentApp02Index),
]