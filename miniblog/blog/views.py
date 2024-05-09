from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginUpForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from .models import Post


# Home Page
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html' , {'posts':posts})


# About Page
def about(request):
    
    return render(request, 'blog/about.html' , )


# About Page
def contact(request):
    
    return render(request, 'blog/contact.html' , )


# Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        return render(request, 'blog/dashboard.html' , {'posts':posts} )
    else:
        return HttpResponseRedirect('/login/')


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


# Add New Post

def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title=title,  desc=desc)
                pst.save()
                # form = PostForm()
                return HttpResponseRedirect('/dashboard/')
        else:
            form = PostForm()
        
        return render(request, "blog/addpost.html", {'form':form})
    else:
        return HttpResponseRedirect('/login/')


# Add Update Post

def update_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        
        return render(request, "blog/updatepost.html", {'form':form})
    else:
        return HttpResponseRedirect('/login/')
# Add Update Post

def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect("/login/")
