from django.urls import path
from . import views
#from .views import VentasView

urlpatterns = [
    
   
   #path('', VentasView.as_view(), name='Ventas'),
   path('', views.ventas_view, name='Ventas'),
   path('clientes/', views.clientes_view, name='Clientes'),
   path('add_cliente/', views.add_cliente_view, name='AddCliente'),
   path('edit_cliente/', views.edit_cliente_view, name='EditCliente'),
   path('delete_cliente/', views.delete_cliente_view, name='DeleteCliente'),
   path('productos/', views.productos_view, name='Productos'),
   path('add_producto/', views.add_producto_view, name='AddProducto'),
   path('edit_producto/', views.edit_producto_view, name='EditProduct'),
   path('delete_product/', views.delete_producto_view, name='DeleteProducto'),
   #path('export/', views.export_pdf_view, name="ExportPDF" ),
   #path('export/<id>/<iva>', views.export_pdf_view, name="ExportPDF" ),
   path('delete_venta/', views.delete_venta_view, name='DeleteVenta'),
   path('Edit_venta/', views.edit_egreso_view, name='EditeVenta'),
   path('Consultas()', views.consultas_view, name='Consultas'),  
   path('delete_consulta/', views.delete_consulta_view, name='DeleteConsulta'),
   
]