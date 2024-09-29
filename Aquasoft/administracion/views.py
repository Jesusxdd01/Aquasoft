from django.shortcuts import render, redirect, get_object_or_404
from administracion.models import Cliente, Egreso, Producto, Egreso, Contacto
from clientes.models import Usuario
from administracion.forms import AddClienteForms, EditarClienteForms, AddProductoForms, EditarProductoForms
from ventas.forms import EditarEgresoForms
from django.contrib import messages
from django.views.generic import ListView, TemplateView
from django.http import JsonResponse, HttpResponse
from weasyprint.text.fonts import FontConfiguration
from django.template.loader import get_template
from weasyprint import HTML, CSS
from django.conf import settings
import os, json
from django.contrib.auth.decorators import login_required

def ventas_view(request):
    venta = Egreso.objects.all()
    num_ventas = len(venta)
    cliente= Usuario.objects.all()
    context =  {
        'venta' : venta,
        'num_ventas' : num_ventas,
        'cliente': cliente
    }
    return render(request,'ventas.html',context)

def delete_venta_view(request):
    if request.POST:
        venta = Egreso.objects.get(pk=request.POST.get('id_producto_eliminar'))
        venta.delete()
    return redirect('Ventas')

def edit_egreso_view(request):
    if request.POST:
        egreso = Egreso.objects.get(pk=request.POST.get('id_egreso_editar'))
        form = EditarEgresoForms(request.POST, request.FILES, instance= egreso) 
        if form.is_valid():
            form.save()      
    return redirect('Ventas')

def clientes_view(request):
    clientes = Usuario.objects.all()
    form_personal = AddClienteForms()
    form_editar = EditarClienteForms()

    context = {
        'clientes':clientes,
        'form_personal': form_personal,
        'form_editar' : form_editar

    }
    return render(request,'clientes.html', context)



def add_cliente_view(request):
    #print("guardar cliente")
    if request.POST:
        form = AddClienteForms(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request, "Error al guardar el cliente")
                return redirect('Clientes')
    return redirect('Clientes')

def edit_cliente_view(request):
    if request.POST:
        cliente = Usuario.objects.get(pk=request.POST.get('id_personal_editar'))
        form = EditarClienteForms(request.POST, request.FILES, instance= cliente) 
        if form.is_valid():
            form.save()      
    return redirect('Clientes')



def delete_cliente_view(request):
    if request.POST:
        cliente = Usuario.objects.get(pk=request.POST.get('id_personal_eliminar'))
        cliente.delete()
    return redirect('Clientes')


def productos_view(request):
    productos = Producto.objects.all()
    form_add = AddProductoForms()
    form_editar = EditarProductoForms()
    context = {
        'productos' : productos,
        'form_add' : form_add,
        'form_editar': form_editar,

    }
    return render(request,'productos.html', context)

def add_producto_view(request):
    #print("guardar cliente")
    if request.POST:
        form = AddProductoForms(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request, "Error al guardar el producto")
                return redirect('Productos')
    return redirect('Productos')

def edit_producto_view(request):
    if request.POST:
        producto= Producto.objects.get(pk=request.POST.get('id_producto_editar'))
        form = EditarProductoForms(request.POST, request.FILES, instance= producto) 
        if form.is_valid():
            form.save()      
    return redirect('Productos')

def delete_producto_view(request):
    if request.POST:
        producto = Producto.objects.get(pk=request.POST.get('id_producto_eliminar'))
        producto.delete()
    return redirect('Productos')


def edit_egreso_view(request):
    if request.POST:
        egreso = Egreso.objects.get(pk=request.POST.get('id_egreso_editar'))
        form = EditarEgresoForms(request.POST, request.FILES, instance= egreso) 
        if form.is_valid():
            form.save()      
    return redirect('Ventas')

def consultas_view(request):
    contacto = Contacto.objects.all()
    num_contacto = len(contacto)
    context =  {
        'contacto' : contacto,
        'num_contacto' : num_contacto,
    }
    return render(request,'consultas.html',context)

def delete_consulta_view(request):
    if request.POST:
        consulta = Contacto.objects.get(pk=request.POST.get('id_consulta'))
        consulta.delete()
    return redirect('Consultas')