from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm


# Home Page
def home(request):
    
    return render(request, 'blog/home.html' , )


# About Page
def about(request):
    
    return render(request, 'blog/about.html' , )


# About Page
def contact(request):
    
    return render(request, 'blog/contact.html' , )


# Dashboard
def dashboard(request):
    
    return render(request, 'blog/dashboard.html' , )


# logout
def user_logout(request):
    
    return HttpResponseRedirect("/")


# Signup
def user_signup(request):
    form = UserCreationForm()
    
    return render(request, 'blog/signup.html' , {"form":form })

# login
def user_login(request):
    
    return render(request, 'blog/login.html' , )


