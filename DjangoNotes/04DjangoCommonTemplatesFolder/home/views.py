from django.shortcuts import render

# Create your views here.
def home_index(request):
    """
    Render the index page for the home app.
    """
    return render(request, 'home/index.html')  # Ensure the template exists in the correct directory