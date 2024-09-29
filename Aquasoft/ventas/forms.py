from django import forms
from administracion.models import Cliente, Producto, Egreso, Contacto
from django.contrib.auth import get_user_model

User = get_user_model()
class EditarEgresoForms(forms.ModelForm):
    class Meta:
        model = Egreso
        fields = ['fecha_pedido', 'cliente', 'producto', 'precioUnitario', 'cantidad', 'total', 'comentarios']
        labels = {
            'fecha_pedido': 'Fecha: ',
            'cliente': 'Nombre: ',
            'producto': 'Producto: ',
            'precioUnitario': 'Precio Unitario',
            'cantidad': 'Cantidad: ',
            'total': 'Total',
            'comentarios': 'Comentarios: ',
        }
        widgets = {
            'fecha_pedido': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'fecha'}),
            'producto': forms.Select(attrs={'class': 'input-text', 'id': 'producto_id', 'onchange': 'actualizarPrecio()'}),
            'precioUnitario': forms.NumberInput(attrs={'class': 'input-text', 'readonly': 'readonly', 'id': 'precioUnitario'}),
            'cantidad': forms.NumberInput(attrs={'class': 'input-text', 'min': '1', 'value': '1','id': 'cantidad', 'onchange': 'calcularTotal()'}),
            'total': forms.NumberInput(attrs={'class': 'input-text', 'readonly': 'readonly', 'id': 'total'}),
            'comentarios': forms.Textarea(attrs={'class': 'input-text', 'id': 'comentarios'}),
        }

    # Sobrescribe el campo 'cliente' para que sea de solo lectura en el formulario
    cliente = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.TextInput(attrs={'class': 'input-text', 'readonly': 'readonly', 'id': 'cliente'}))
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['cliente'].initial = user
            self.fields['cliente'].queryset = User.objects.filter(id=user.id)
            self.fields['cliente'].widget.attrs['value'] = user.username


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'telefono', 'correo','tipoConsulta', 'mensaje', 'avisos']
        labels = {
            'nombre' : 'Nombre',
            'telefono' : 'Teléfono',
            'correo': 'Correo',
            'tipoConsulta' : 'Asunto', 
            'mensaje': 'Mensaje', 
            'avisos' : 'Aviso',          
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'input-text', 'id': 'nombre'}),
            'telefono': forms.TextInput(attrs={'class': 'input-text', 'id': 'telefono'}),
            'correo': forms.EmailInput(attrs={'class': 'input-text', 'id': 'email'}),
            'tipoConsulta': forms.Select(attrs={'class': 'input-text', 'id': 'asunto'}),
            'mensaje': forms.Textarea(attrs={'class': 'input-text', 'id': 'mensaje'}),
            
        }