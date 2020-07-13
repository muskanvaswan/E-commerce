from django.urls import path, include

from . import views

urlpatterns = [
    path("<int:item_id>/", views.item, name="item"),
    path('<int:item_id>/add/', views.add, name="add"),
    path("cart/", views.cart, name="cart"),
    path("empty/", views.empty_cart, name="empty"),
    path("order/", views.order, name="order")
]
