from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        if User.objects.filter(username=username ).exists():
            return render(request, 'regis/signup.html', {'error': 'Username already exists'})
        if User.objects.filter(email=email).exists():
            return render(request, 'regis/signup.html', {'error': 'Email already exists'})
        
        
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        login(request, user)
        return redirect('login')
        
    return render(request, 'regis/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'regis/login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'regis/login.html')

def dashboard(request):
    return render(request,'regis/dashboard.html')

def user_logout(request):
    logout(request)
    return redirect('login')





