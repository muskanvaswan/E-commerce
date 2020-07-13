from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Item, Category

# Create your views here.
def index(request):
    return render(request, "dashboard/index.html");

def menu(request):
    context ={
        "items": Item.objects.all(),
        "categories": Category.objects.all(),
    }
    return render(request, "dashboard/menu.html", context)

def type(request, category_id):
    category = Category.objects.get(pk=category_id)
    context={
        "items": category.Things.all(),
        "categories": Category.objects.all(),
    }
    return render(request, "dashboard/menu.html", context)

def search(request):
    name = request.POST["q"]
    items = Item.objects.all()
    result = []
    for item in items:
        if name in item.Name:
            result.append(item)
    context = {
        "items": result,
        "categories": Category.objects.all(),
    }
    return render(request, "dashboard/menu.html", context)

def profile(request):
    context = {
        "orders": request.user.orders.all(),
        "viewed": request.user.recently_viewed.all(),
    }
    return render(request, "cart/profile.html", context)

def login_view(request):
    return render(request, "dashboard/login.html")

def login_auth(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "dashboard/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
