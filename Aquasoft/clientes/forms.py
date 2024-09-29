from django import forms
from clientes.models import Usuario

class usuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario

        fields=[
            'nombre',
            'apPaterno',
            'apMaterno',
            'direccion',
            'telefono',
            'email',
            'contraseña',
        ]
        labels={
            'nombre':'Nombre',
            'apPaterno':'Apellido Paterno',
            'apMaterno': 'Apellido Materno',
            'direccion':'Direccion de casa',
            'telefono':'Telefono',
            'email':'Correo electronico',
            'contraseña':'Contraseña'
        }
        '''
        widget={

        }
        '''
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})

class logForm(forms.Form):
    class Meta:
        fields=[
            'email',
            'contraseña',
        ]
        
        labels={
            'email':'Email del usuario',
            'contraseña': 'Contraseña del usuario'
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})

class UsuarioUpdate(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'direccion', 'telefono', 'email', 'contraseña']