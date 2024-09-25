from django.db import models
from django.core.validators import MinValueValidator


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
    price = models.FloatField(null=False, validators=[MinValueValidator(0)])
    brand = models.CharField(max_length=20,null=True)
    category = models.CharField(max_length=20, choices=PRODUCT_TYPES)
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    image = models.ImageField(null=True,upload_to='product/')

    def __str__(self):
        return self.name

