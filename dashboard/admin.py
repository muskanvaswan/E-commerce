from django.contrib import admin

from .models import Item, Vendor, Category
# Register your models here.
admin.site.register(Item)
admin.site.register(Vendor)
admin.site.register(Category)
