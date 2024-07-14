# from django.contrib.auth import login
# from django.shortcuts import render, redirect
# from .forms import CustomUserCreationForm

# Create your views here.

# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home') 
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm


# Create your views here.
# Home page
def index(request):
    return render(request, 'home.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'registration/register.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')


# About Us page
def about(request):
    return render(request, 'about.html')