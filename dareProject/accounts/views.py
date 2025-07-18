from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def register(req):
    if req.method == "POST":
        username = req.POST.get("username")
        email = req.POST.get("email")
        password = req.POST.get("password")

        new_user = User.objects.create(
            username = username,
            email = email
        )

        new_user.set_password(password)

        new_user.save()

        return redirect('home')
    return render(req, 'accounts/register.html')

def login_view(req):
    if req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")

        pass

def logout_view(req):
    if req.method == "POST":
        # Assuming you have a logout function in your views
        return redirect('home')
    return render(req, 'accounts/logout.html')