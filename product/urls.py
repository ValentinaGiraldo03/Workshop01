# product/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('category/<str:categoryName>', views.productsByCategory, name='productsByCategory'),
    path('product/<int:id>/', views.productDetail, name='productDetail'),
]
