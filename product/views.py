from django.shortcuts import render, get_object_or_404
from .models import Product

def productsByCategory(request, categoryName):
    products = Product.objects.filter(category=categoryName)
    return render(request, 'productsByCategory.html', {'category': categoryName, 'products': products})


def productDetail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'productDetail.html', {'product': product})

