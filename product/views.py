from django.shortcuts import render, get_object_or_404
from .models import Product
from review.models import Review
from review.forms import ReviewForm
from user.models import Client

def productsByCategory(request, categoryName):
    products = Product.objects.filter(category=categoryName)
    return render(request, 'productsByCategory.html', {'category': categoryName, 'products': products})


def productDetail(request, id):
    reviews = Review.objects.filter(productReviewed=Product.objects.get(id=id))
    product = get_object_or_404(Product, id=id)
    sent_review = None
    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            sent_review = review_form.save(commit=False)
            sent_review.productReviewed = product
            sent_review.reviewingClient = Client.objects.get(user=request.user)
            sent_review.save()
    else:
        review_form = ReviewForm()
    
    return render(request, 'productDetail.html', {'product': product,
                                                    'reviews': reviews,
                                                    'review_form': review_form,
                                                    'sent_review': sent_review})

