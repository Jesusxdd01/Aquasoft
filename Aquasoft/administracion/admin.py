from django.contrib import admin
from administracion.models import Cliente, Producto ,Empresa, Egreso, Contacto

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'codigo')
    search_fields = ['nombre']
    readonly_fields = ('created', 'updated')
    filter_horizontal= ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Cliente, ClienteAdmin)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'cantidad', 'costo')
    search_fields = ['descripcion']
    readonly_fields = ('created', 'updated')
    filter_horizontal= ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Producto, ProductoAdmin)

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'domicilio', 'telefono')
    search_fields = []
    readonly_fields = ('created', 'updated')
    filter_horizontal= ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Empresa,EmpresaAdmin)



class EgresoAdmin(admin.ModelAdmin):
    list_display = ('fecha_pedido', 'cliente', 'total', 'pagado', 'comentarios', 'ticket', 'desglosar')
    search_fields = []
    readonly_fields = ('created', 'updated')
    filter_horizontal= ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Egreso,EgresoAdmin)

admin.site.register(Contacto)