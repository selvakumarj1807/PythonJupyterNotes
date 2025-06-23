from django.shortcuts import render

# Create your views here.
def studentApp03Index(request):
    return render(request, 'studentApp03/index.html')  # Ensure the template exists in the correct directory