from django.shortcuts import redirect, render

from app.models import Doctor

# Create your views here.

from .forms import AppoitmentForm

def index(request):
    # Handle appointment form submission
    if request.method == "POST":
        form = AppoitmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to homepage or success page
    else:
        form = AppoitmentForm()

    doctors = Doctor.objects.filter(status=True)  # Get active doctors
    context = {
        'form': form,
        'doctors': doctors
    }
    return render(request, 'index.html', context)

def doctor(request):
    doctors = Doctor.objects.filter(status=0)
    return render(request, 'doctors.html', {'doctors': doctors})