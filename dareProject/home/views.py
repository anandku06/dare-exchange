from django.shortcuts import render, redirect
from .models import DareExchange


# Create your views here.
def home(req):
    return render(req, "home.html")


def create_dare(req):
    if req.method == "POST":
        dare_title = req.POST.get("title")
        dare_description = req.POST.get("description")
        dare_category = req.POST.get("category")
        dare_difficulty = req.POST.get("difficulty")

        newDare = DareExchange(
            title=dare_title,
            description=dare_description,
            category=dare_category,
            difficulty=dare_difficulty,
        )

        newDare.save()
        return redirect("show_dares")

    return render(req, "create_dare.html")


def show_dares(req):
    dares = DareExchange.objects.all()

    return render(req, "showDares.html", {"dares": dares})


def delete_dare(req, id):
    if req.method == "POST":
        try:
            dare = DareExchange.objects.get(id=id)
            dare.delete()
        except DareExchange.DoesNotExist:
            pass
    return redirect("show_dares")

def update_dare(req, id):
    dare = DareExchange.objects.get(id=id)

    if req.method == "POST":
        dare.title = req.POST.get("title")
        dare.description = req.POST.get("description")
        dare.category = req.POST.get("category")
        dare.difficulty = req.POST.get("difficulty")

        dare.save()

        return redirect("show_dares")

    return render(req, 'edit-dare.html', {"dare" : dare})