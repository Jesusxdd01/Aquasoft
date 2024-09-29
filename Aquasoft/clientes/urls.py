from django.urls import path
from . import views
from .views import MisPedidosListView,GenerarTicketView,UsuarioUpdateView,DescargarTicketPDFView


urlpatterns = [
   path('login/', views.userLog, name='userIn'),
   path('logout/', views.userOut, name='userOut'),
   path('misPedidos/', MisPedidosListView.as_view(), name='misPedidos'),
   path('generar-ticket/<int:egreso_id>/', GenerarTicketView.as_view(), name='generar_ticket'),
   path('usuario/update/', UsuarioUpdateView.as_view(), name='usuarioUpdate'),
    path('ticket/<int:egreso_id>/pdf/', DescargarTicketPDFView.as_view(), name='descargar_ticket_pdf'),
   path('create/usuario/', views.usuarioCreate, name='usuarioCreate'),
   path('delete_venta/', views.delete_venta_view, name='DeleteVentaC'),
]