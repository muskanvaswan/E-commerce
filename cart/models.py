from django.db import models
from django.contrib.auth.models import User

from dashboard.models import Item
# Create your models here.
class Cart(models.Model):

    item = models.ForeignKey(Item, related_name="items", on_delete=models.CASCADE)
    user = models.ManyToManyField(User, related_name="cart")

    def __str__(self):
        return f" {self.item}"

class Order(models.Model):
    statuses = [('placed_order', 'PO'),('on_the_way', 'OTW'), ('delivered', 'D'), ('Cancelled','C')]
    item = models.ForeignKey(Item, related_name="orders", on_delete=models.CASCADE)
    user = models.ManyToManyField(User, related_name="orders")
    status = models.CharField( max_length = 50, choices=statuses, default="placed_order")
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"Ordered {self.item}"
