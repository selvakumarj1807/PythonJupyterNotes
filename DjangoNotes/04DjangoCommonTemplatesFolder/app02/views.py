from django.shortcuts import render

# Create your views here.

def app02_index(request):
    """
    Render the index page for app02.
    """
    return render(request, 'app02/index.html')  # Ensure the template exists in the correct directory