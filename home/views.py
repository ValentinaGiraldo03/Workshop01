from django.shortcuts import render
from product.models import Product


def home_view(request):
    products = Product.objects.all()  
    return render(request, 'home.html', {'products': products})
