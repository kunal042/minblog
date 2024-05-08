from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginUpForm
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout


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
    logout(request)
    
    return HttpResponseRedirect("/")


# Signup
def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            un = form.cleaned_data['username']
            fn = form.cleaned_data['first_name']
            ln = form.cleaned_data['last_name']
            em = form.cleaned_data['email']
            

            messages.success(request, "Congartulations!! Yor become an Author.")
            
            form.save()
        form = SignUpForm()
    else:
        form = SignUpForm()
    
    return render(request, 'blog/signup.html' , {"form":form })

# login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginUpForm(request=request, data=request.POST)
            if form.is_valid():
                un = form.cleaned_data['username']
                upass = form.cleaned_data["password"]
                user = authenticate(username=un, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginUpForm()
        return render(request, 'blog/login.html' ,  {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')

