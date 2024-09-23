from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/client/', views.register_client, name='register_client'),
    path('register/administrator/', views.register_administrator, name='register_administrator'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('addProduct/', views.agregar_producto, name='agregar_producto'),
    path('editProduct/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('deleteProduct/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]
