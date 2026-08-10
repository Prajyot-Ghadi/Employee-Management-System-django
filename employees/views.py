from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required


# Create your views here.

# Decide which url pattern to create
# created url pattern in the main urls.py and forwared it to employees.url
#create the view
#create the template

@login_required
def employee_detail(request,id):

    employee = get_object_or_404(Employee, id=id)
    
    context = {
        'employee' : employee
    }
    
    return render(request, 'employee_detail.html', context)


@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

        else:
            print(form.errors)

    else:
        form = EmployeeForm()
    context = {
        'form' : form,
    }
    return render(request, 'add_employee.html', context)


@login_required
def update_employee(request, id):

    employee = get_object_or_404(Employee, id = id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)

        if form.is_valid():
            form.save()
            return redirect('home')
            
        else:
            print(form.errors)
    

    else:
        form = EmployeeForm(instance=employee)
        
    context = {
                'form':form,
                'employee':employee
                
            }
    return render(request, 'update_employee.html', context)

@login_required
def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    employee.delete()

    return redirect('home')