from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def register(req):
    if req.method == "POST":
        username = req.POST.get("username")
        email = req.POST.get("email")
        password = req.POST.get("password")

        if User.objects.filter(username=username).exists() or User.objects.filter(email).exists():
            messages.add_message(req, messages.ERROR, "Username or Email already exists")
            return render(req, 'accounts/register.html', {"messages" : messages})

        new_user = User.objects.create(
            username = username,
            email = email
        )

        new_user.set_password(password)

        new_user.save()
        login(req, new_user)
        return redirect('home')
    return render(req, 'accounts/register.html')

def login_view(req):
    if req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")
    
    return render(req, "accounts/login.html")



def logout_view(req):
    logout(req)
    return redirect('home')