from django import forms
from administracion.models import Cliente, Producto, Egreso


class AddClienteForms(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo', 'nombre', 'email','telefono','direccion')
        labels = {
            'codigo': 'Codigo cliente: ',
            'nombre': 'Nombre Cliente: ',
            'email': 'Email: ',
            'telefono' : 'Telefono (contacto): ',
            'direccion' : 'Direccion: ',
        }


class EditarClienteForms(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo', 'nombre', 'email','telefono','direccion')
        labels = {
            'codigo': 'Codigo cliente: ',
            'nombre': 'Nombre Cliente: ',
            'email': 'Email: ',
            'telefono' : 'Telefono (contacto): ',
            'direccion' : 'Direccion: ',
        }
        widgets = {
            'codigo' : forms.TextInput(attrs={'type': 'text', 'id': 'codigo_editar'}),
            'nombre' : forms.TextInput(attrs={'id': 'nombre_editar'}),
            'email' : forms.TextInput(attrs={'id': 'email_editar'}),
            'telefono' : forms.TextInput(attrs={'id': 'telefono_editar'}),
            'direccion' : forms.TextInput(attrs={'id': 'direccion_editar'}),
        }

class AddProductoForms(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo','descripcion', 'precio', 'imagen','detalle')
        labels = {
            'codigo': 'Codigo Producto: ',
            'descripcion': 'Descripción de producto: ',
            'precio' : 'Precio: ',
            'imagen' : 'Imagen: ',
            'detalle': 'Detalle',
            
       }

class EditarProductoForms(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo','descripcion',  'precio','imagen','detalle')   
        labels = {
            'codigo': 'Codigo Producto: ',
            'descripcion': 'Descripción de producto: ',
            'precio' : 'Precio: ',
            'imagen' : 'Imagen: ',
            'detalle': 'Detalle',
            
            
        }
        widgets = {
            'codigo' : forms.TextInput(attrs={'type': 'text', 'id': 'codigo_editar'}),
            'descripcion' : forms.TextInput(attrs={'id': 'descripcion_editar'}),
            'precio' : forms.TextInput(attrs={'id': 'precio_editar'}),
            'detalle' : forms.TextInput(attrs={'id': 'detalle_editar'}),
        
        }