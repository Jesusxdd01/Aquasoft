from django.db import models


class Usuario(models.Model):
   
    nombre = models.CharField(max_length=150,null=True, blank=True)
    apPaterno = models.CharField(max_length=200, null=True, blank=True)
    apMaterno = models.CharField(max_length=200, null=True, blank=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=10)
    email = models.EmailField()
    contraseña = models.CharField(max_length=25, help_text='Maximo 25 caracteres')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    OPCIONES_ROL = [
        ('usuario', 'Usuario normal'),
        ('admin', 'Administrador'),
    ]
    roles = models.CharField(max_length=7, choices=OPCIONES_ROL, default='usuario')

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    def __str__(self):
        return f"{self.nombre}"