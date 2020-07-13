from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Name}"

class Vendor(models.Model):
    Name = models.CharField(max_length=200)
    Address = models.CharField(max_length=500, null=True)
    Phone = models.IntegerField(null=True)

class Item(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=2000, null=True)
    Warranty = models.CharField(max_length=50, null=True)
    Return = models.CharField(max_length=50, null=True)
    vendor = models.ManyToManyField(Vendor, related_name="Items")
    type = models.ManyToManyField(Category, related_name="Things")
    Cost = models.DecimalField(max_digits=5, decimal_places=2, default=0.01)
    recently_viewed = models.ManyToManyField(User, related_name="recently_viewed", max_length=10)

    def __str__(self):
        return f"{self.Name}"
