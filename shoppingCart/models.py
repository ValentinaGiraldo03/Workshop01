from django.db import models
from product.models import Product
from user.models import Client


class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=Client.objects.first().id)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'