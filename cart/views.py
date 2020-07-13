from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User

from dashboard.models import Item
from .models import Cart, Order

# Create your views here.
def item(request, item_id):
    i = Item.objects.get(pk= item_id)
    if request.user.is_authenticated:
        request.user.recently_viewed.add(i)
    context = {
        "item": i
    }
    return render(request, "cart/item.html", context)

def add(request, item_id):

    i = Item.objects.get(pk= item_id)
    if request.user.is_authenticated:
        c = Cart(item = i)
        c.save()
        request.user.cart.add(c)
        return redirect("cart")
    else:
        context ={
            "message": "You need to sign in to complete this action",
            "item" : i
        }
        return render(request, "cart/item.html", context)

def cart(request):
    Items = request.user.cart.all()
    total = 0
    for items in Items:
        total += items.item.Cost
    context = {
        "items": Items,
        "total": total
    }
    return render(request, "cart/cart.html", context)

def empty_cart(request):
    items = request.user.cart.all()
    for i in items:
        i.delete()
    return redirect("cart")

def order(request):
    Items = request.user.cart.all()
    for item in Items:
        o = Order(item = item.item)
        o.save()
        request.user.orders.add(o)
    return redirect("empty")
