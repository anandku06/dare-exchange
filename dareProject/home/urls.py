from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.create_dare, name="create_dare"),
    path("dares/", views.show_dares, name="show_dares")
]
