from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginUpForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import Group
from .models import Post


# Home Page
def home(request):
    posts = Post.objects.all()
    user = request.user
    full_name = user.get_username()
    gps = user.groups.all()
    return render(request, 'blog/home.html' , {'posts':posts, "full_name":full_name, 'gps':gps})


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
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'blog/dashboard.html' , {'posts':posts, 'full_name':full_name, 'gps':gps} )
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
            
            messages.success(request, "Congartulations!! Yor become an Author.")
            
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)

        
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
