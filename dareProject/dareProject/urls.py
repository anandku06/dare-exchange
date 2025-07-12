from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("about_us/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("features/", views.feature, name="features"),
]
