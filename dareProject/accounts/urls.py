from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.register, name="account"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", include('dashboard.urls'))
]