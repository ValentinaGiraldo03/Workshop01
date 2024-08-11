from django.db import models
from product.models import Product
from user.models import Client


# Create your models here.
class shoppingCart(models.Model):

    products = models.ManyToManyField(Product, through='CartProduct')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

class CartProduct(models.Model):
    cart = models.ForeignKey(shoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = ('cart', 'product')
