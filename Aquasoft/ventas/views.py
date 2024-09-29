from django.shortcuts import render, redirect, get_object_or_404
from administracion.models import  Producto
from .forms import EditarEgresoForms, ContactoForm
from django.contrib import messages
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponse
from weasyprint.text.fonts import FontConfiguration
from django.template.loader import get_template
from weasyprint import HTML, CSS
from django.conf import settings
import os, json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.contrib.auth import get_user_model


# Create your views here.

def inicio(request):
    return render(request, 'index.html')
    
def blog(request):
    return render(request, 'blog.html')

def contacto(request):
    return render(request, 'contacto.html')

def login(request):
    return render(request, 'login.html')

def pedidos(request):
    return render(request, 'pedidos.html')

def puntos(request):
    return render(request, 'puntosVenta.html')

def preguntas(request):
    return render(request, 'preguntas.html')

def productosPagina(request):
    return render(request, 'productoPagina.html')

def productosPedido_view(request):
    productos = Producto.objects.all()
    
    context = {
        'productos' : productos,
    
    }
    return render(request,'productoPagina.html', context)


class RegistrarPedidosView(LoginRequiredMixin, View):
    login_url = 'userIn'

    def get(self, request, producto_id):
        producto = get_object_or_404(Producto, pk=producto_id)
        form = EditarEgresoForms(initial={'producto': producto, 'precioUnitario': producto.precio}, user=request.user)
        return render(request, 'pedidoPrueba.html', {'form': form})

    def post(self, request, producto_id):
        producto = get_object_or_404(Producto, pk=producto_id)
        form = EditarEgresoForms(request.POST, user=request.user)
        if form.is_valid():
            egreso = form.save(commit=False)
            egreso.cliente = request.user
            egreso.producto = producto
            egreso.total = egreso.cantidad * egreso.precioUnitario
            egreso.save()
            return redirect('generar_ticket', egreso_id=egreso.id)  # Redirigir a la vista de generación de ticket
        return render(request, 'pedidoPrueba.html', {'form': form})

def obtener_precio(request):
    if request.method == 'GET' and 'producto_id' in request.GET:
        producto_id = request.GET['producto_id']
        producto = get_object_or_404(Producto, pk=producto_id)
        return JsonResponse({'precio': producto.precio})
    else:
        return JsonResponse({'error': 'Parámetro "producto_id" no proporcionado'}, status=400)
    
def contacto_view(request):        
    form = ContactoForm()  # Inicializa el formulario fuera de la lógica condicional
    
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('contacto')  # Redirige a la misma página (o a donde sea necesario) después de enviar el formulario
              
    return render(request, 'contacto.html', {'form': form})