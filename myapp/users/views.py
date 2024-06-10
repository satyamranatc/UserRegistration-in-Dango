# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm, SigninForm
from .models import User

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('signin')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username, password=password).first()
            if user:
                messages.success(request, 'Welcome, {}'.format(username))
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = SigninForm()
    return render(request, 'signin.html', {'form': form})

def home(request):
    return render(request, 'home.html')
