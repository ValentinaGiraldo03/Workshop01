from django.urls import path
from . import views

app_name = 'billing'

urlpatterns = [
    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
]