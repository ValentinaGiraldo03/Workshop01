from django.shortcuts import render
from product.models import Product


def home_view(request):
    if request.method == 'GET':
        filter = request.GET.get('filter')
        if filter:
            products = Product.objects.filter(name__icontains=filter)
            return render(request, 'home.html', {'products': products})
    products = Product.objects.all()  
    return render(request, 'home.html', {'products': products})