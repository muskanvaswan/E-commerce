from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("autherize/", views.login_auth, name="autherize"),
    path("logout/", views.logout_view, name="logout"),
    path("login/", views.login_view, name="login"),
    path("shop/", views.menu, name="menu"),
    path("type/<int:category_id>", views.type, name="type"),
    path("search", views.search, name="search"),
    path("profile", views.profile, name="profile")
]
