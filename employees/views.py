from django.shortcuts import render, get_object_or_404
from .models import Employee



# Create your views here.

# Decide which url pattern to create
# created url pattern in the main urls.py and forwared it to employees.url
#create the view
#create the template

def employee_detail(request,id):

    employee = get_object_or_404(Employee, id=id)
    
    context = {
        'employee' : employee
    }
    
    return render(request, 'employee_detail.html', context)