from django.urls import path
from . import views
from .views import RegistrarPedidosView

urlpatterns = [
   
   path('', views.inicio, name='inicio'),
   #path('pedidos/<int:producto_id>/', views.registrarPedidos_view, name='pedidoPrueba'),
   path('pedidos/<int:producto_id>/', RegistrarPedidosView.as_view(), name='pedidoPrueba'),
   #path('productosPagina/', views.productosPagina, name='productosPagina'),
   path('productosPagina/', views.productosPedido_view, name='productosPagina'),
   path('puntos/', views.puntos, name='puntos'),
   path('blog/', views.blog, name='blog'),
   #path('contacto/', views.contacto, name='contacto'),
   path('preguntas/', views.preguntas, name='preguntas'),
   path('obtener_precio/', views.obtener_precio, name='obtener_precio'),
   path('contacto/',views.contacto_view, name='contacto')
]