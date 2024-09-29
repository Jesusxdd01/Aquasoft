from django.shortcuts import render, redirect, get_object_or_404
from clientes.forms import usuarioForm, logForm, UsuarioUpdate
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from clientes.models import Usuario
from weasyprint.text.fonts import FontConfiguration
from weasyprint import HTML, CSS
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from administracion.models import Egreso  # Asegúrate de importar el modelo Egreso correctamente
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views import View
import tempfile


# Create your views here.
def userLog(request):
    if request.method == 'POST':
        form = logForm(request.POST)
        if form.is_valid():
            user = authenticate(request,
                                username=request.POST['email'],
                                password=request.POST['contraseña'])
            if user is None:
                return render(request, 'login.html',{'form':form ,
                                                    'error':'La contraseña o usuario son incorrectos'})
            else:
                login(request,user)
                return redirect('inicio')
    else:
        form = logForm()
    return render(request, 'login.html',{'form':form})

def usuarioCreate(request):
    if request.method == 'POST':
        form = usuarioForm(request.POST)
        if form.is_valid():
            if request.POST['contraseña'] == request.POST['contraseña2']:
                try:
                    user = User.objects.create_user(username=request.POST['email'],
                                                    password=request.POST['contraseña'],
                                                    first_name=request.POST['nombre'],
                                                    last_name=request.POST['apPaterno'],
                                                    email=request.POST['email'])
                    user.save()
                    form.save()
                    login(request,user)
                    return redirect('inicio')
                except IntegrityError:
                    return render(request, 'createUsuarios.html',{'form':form,
                                                                  'error':'El usuario ya existe'})
            return render(request, 'createUsuarios.html',{'form':form,
                                                          'error':'Las contraseñas no coinciden'})            
    else:
        form = usuarioForm()
    return render(request, 'createUsuarios.html',{'form':form})


    
def userOut(request):
    logout(request)
    return redirect ('inicio')




class MisPedidosListView(LoginRequiredMixin, ListView):
    model = Egreso
    template_name = 'misPedidos.html'  # Reemplaza 'mis_pedidos.html' con la plantilla adecuada
    context_object_name = 'pedidos'  # Nombre del objeto de contexto en la plantilla

    def get_queryset(self):
        # Obtén los pedidos del usuario actualmente autenticado
        return Egreso.objects.filter(cliente=self.request.user)



class GenerarTicketView(LoginRequiredMixin, View):
    login_url = 'userIn'

    def get(self, request, egreso_id):
        egreso = get_object_or_404(Egreso, pk=egreso_id)
        context = {
            'egreso' : egreso
        }
        print("Datos del egreso:", egreso.__dict__)
        return render(request, 'ticket.html', context)

class DescargarTicketPDFView(LoginRequiredMixin, View):
    login_url = 'userIn'

    def get(self, request, egreso_id):
        egreso = get_object_or_404(Egreso, pk=egreso_id)
        context = {
            'egreso': egreso
        }
        html_string = render_to_string('ticket.html', context)
        
        # Crear PDF
        html = HTML(string=html_string)
        result = html.write_pdf()

        # Crear respuesta
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename=ticket_{egreso.id}.pdf'
        response.write(result)
        
        return response

class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    form_class = UsuarioUpdate
    template_name = 'usuarioUpdate.html'  # Ajusta el nombre de la plantilla según tu preferencia
    success_url = 'inicio'  # URL a la que redirigir después de una actualización exitosa

    def get_object(self, queryset=None):
        # Devuelve el objeto del usuario actualmente logueado
        return self.request.user.usuario

def delete_venta_view(request):
    if request.POST:
        venta = Egreso.objects.get(pk=request.POST.get('id_producto_eliminar'))
        venta.delete()
    return redirect('misPedidos')

