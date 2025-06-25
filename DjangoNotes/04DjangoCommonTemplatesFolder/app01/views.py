from django.shortcuts import render

# Create your views here.

def app01_index(request):
    """
    Render the index page for app01.
    """
    return render(request, 'app01/index.html')