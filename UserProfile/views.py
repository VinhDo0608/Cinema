import re
from django.contrib import messages
from django.shortcuts import render, redirect
from UserProfile.models import Address
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signup(request):
    form =  CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Account Created! You can Login')
            return redirect('signin')
    
    context = {'form': form}
    return render(request, 'UserProfile/signup.html', context)

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('checkout')
           
        else:
            messages.info(request, 'Invalid credentials')
            

def signout(request):
    logout(request)
    return redirect('index')
    