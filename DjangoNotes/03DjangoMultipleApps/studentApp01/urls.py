from django.urls import path

from . import views

urlpatterns = [
    path('', views.studentApp01Index),
]