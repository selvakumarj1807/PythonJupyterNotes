from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'product.html')

def table(request):
    return render(request, 'table.html')