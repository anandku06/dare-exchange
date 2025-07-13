from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.create_dare, name="create_dare"),
    path("dares/", views.show_dares, name="show_dares"),
    path("delete/<int:id>/", views.delete_dare, name="delete_dare"),
    path("update/<int:id>/", views.update_dare, name="edit_dare"),
]
