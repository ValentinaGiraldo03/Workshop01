from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, ClientRegisterForm
from product.forms import ProductForm
from product.models import Product  # Corrected import
from .models import Administrator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

# Función para verificar si el usuario es administrador
def is_admin(user):
    return user.is_authenticated and user.is_staff

# Vista para registrar clientes
def register_client(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        client_form = ClientRegisterForm(request.POST)
        if user_form.is_valid() and client_form.is_valid():
            user = user_form.save()
            client = client_form.save(commit=False)
            client.user = user
            client.save()
            login(request, user)
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        client_form = ClientRegisterForm()
    
    return render(request, 'register_client.html', {'user_form': user_form, 'client_form': client_form})

# Vista para registrar administradores
def register_administrator(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            # Guardamos el usuario sin hacer commit aún para modificar el campo 'is_staff'
            user = user_form.save(commit=False)
            user.is_staff = True  # Establecemos que el usuario es administrador
            user.save()  # Ahora sí guardamos el usuario con is_staff=True

            # Creamos la instancia del modelo Administrator
            administrator = Administrator(user=user)
            administrator.save()

            login(request, user)  # Inicia sesión automáticamente
            return redirect('home')  # Redirige al home
    else:
        user_form = UserRegisterForm()
    
    return render(request, 'register_administrator.html', {'user_form': user_form})


# Vista para iniciar sesión
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome {username}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

# Vista para agregar productos (solo administradores)
@user_passes_test(is_admin)
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto agregado exitosamente.')
            return redirect('home')
    else:
        form = ProductForm()
    
    return render(request, 'agregar_producto.html', {'form': form})

# Vista para editar productos (solo administradores)
@user_passes_test(is_admin)
def editar_producto(request, producto_id):
    producto = get_object_or_404(Product, id=producto_id)  # Updated reference to Product
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente.')
            return redirect('home')
    else:
        form = ProductForm(instance=producto)
    
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})

# Vista para eliminar productos (solo administradores)
@user_passes_test(is_admin)
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Product, id=producto_id)  # Updated reference to Product
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
        return redirect('home')
    
    return render(request, 'eliminar_producto.html', {'producto': producto})
