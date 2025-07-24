from django.shortcuts import render
from rest_framework import generics

from app.models import Student
from app.serializers import StudentSerializer

# Create your views here.

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer