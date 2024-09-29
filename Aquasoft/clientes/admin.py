from django.contrib import admin
from clientes.models import Usuario
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email')
    search_fields = ['nombre']
    readonly_fields = ('created', 'updated')
    filter_horizontal= ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Usuario, UsuarioAdmin)