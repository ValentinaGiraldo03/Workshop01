from django.db import models


class Product(models.Model):
    PRODUCT_TYPES = [
        ("Computer", "Computer"),
        ("Screen", "Screen"),
        ("Keyboard", "Keyboard"),
        ("Mouse", "Mouse"),
        ("Printer", "Printer"),
    ]
    name = models.CharField(max_length=30,null=False)
    description = models.CharField(max_length=1000,null=True)
    price = models.FloatField(null=False)
    brand = models.CharField(max_length=20,null=True)
    category = models.CharField(max_length=20, choices=PRODUCT_TYPES)
    stock = models.IntegerField()
    image = models.ImageField(null=True,upload_to='product/')
