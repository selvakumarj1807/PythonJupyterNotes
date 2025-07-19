from django.shortcuts import redirect, render

from app.models import Employee

# Create your views here.

def index(request):
    employees = Employee.objects.all() 
    return render(request, 'index.html', {'employees': employees})
    
def addnew(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        
        employee = Employee(name=name, email=email, contact=contact)
        employee.save()
        
        return redirect('/')
        
    return render(request, 'addnew.html')

def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    
    return redirect('/')