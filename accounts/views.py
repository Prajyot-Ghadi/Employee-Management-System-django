from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import auth

# Create your views here.

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('register')

    else:
        form = UserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/register.html', context)



def login(request):
    if request.method =='POST':
        form  = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('home')

    else:    
        form= AuthenticationForm()

    context = {
        'form' : form
    }

    return render(request, 'accounts/login.html', context)



