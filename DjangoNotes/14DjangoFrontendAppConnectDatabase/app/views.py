from django.shortcuts import render

from app.models import Doctor

# Create your views here.

def index(request):
    return render(request, 'index.html')

def doctor(request):
    doctors = Doctor.objects.filter(status=0)
    return render(request, 'doctors.html', {'doctors': doctors})