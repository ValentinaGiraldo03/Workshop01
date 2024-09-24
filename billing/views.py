from django.shortcuts import render, redirect
from django.http import FileResponse
from reportlab.pdfgen import canvas
from user.models import Client
from shoppingCart.models import CartProduct

# Create your views here.
def generar_pdf(request):
    user = request.user
    response = FileResponse(generate_file(user),
                            as_attachment=True,
                            filename='factura.pdf')
    return response

def generate_file(user):
    from io import BytesIO
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    user = user
    cart = CartProduct.objects.filter(client=Client.objects.get(user=user))
    total_price = sum(item.product.price * item.quantity for item in cart)

    p.drawString(100, 800, f'Factura de {user.first_name} {user.last_name}')
    p.drawString(100, 780, f'Cliente: {user.email}')
    p.drawString(100, 760, 'Productos:')
    y = 710
    for item in cart:
        p.drawString(120, y, f'{item.product.name} x {item.quantity}..........{'${:,.2f}'.format(item.product.price*item.quantity)}')
        y -= 50
    p.drawString(100, y, f'Total: {'${:,.0f}'.format(total_price)}')
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer

