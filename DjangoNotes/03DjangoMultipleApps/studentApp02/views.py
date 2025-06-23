from django.shortcuts import render

# Create your views here.

def studentApp02Index(request):
    return render(request, 'studentApp02/index.html')