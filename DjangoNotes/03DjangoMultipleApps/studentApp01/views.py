from django.shortcuts import render

# Create your views here.
def studentApp01Index(request):
    return render(request, 'studentApp01/index.html')