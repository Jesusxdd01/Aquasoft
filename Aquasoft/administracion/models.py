from django.db import models
from django.forms import model_to_dict
from django.contrib.auth import get_user_model

class Cliente(models.Model):
    codigo = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(default="@gmail.com")
    nombre = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=200, null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='cliente'
        verbose_name_plural = 'clientes'
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=200, unique=True, null=True, blank=True)
    descripcion = models.CharField(max_length=200, unique=True, null=True, blank=False)
    detalle = models.CharField(max_length=1000,null=True,blank=True)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)
    costo = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    precio = models.DecimalField(max_digits=20, decimal_places=2, null=False, default=0, blank=True)
    cantidad = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='producto'
        verbose_name_plural = 'productos'
    
    def __str__(self):
        return "%s - %s" % (self.descripcion, self.precio)    

User=get_user_model()
class Egreso(models.Model):
    fecha_pedido = models.DateField()
    cliente = models.ForeignKey(User, on_delete=models.SET_NULL , null=True )
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL , null=True , related_name='producto')
    precioUnitario = models.DecimalField(max_digits=20, decimal_places=2,null=True)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    pagado = models.CharField(max_length=2, choices=(('si', 'Sí'), ('no', 'No')), default='no')
    comentarios = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    ticket = models.BooleanField(default=True)
    desglosar = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=True , null=True)

    class Meta:
        verbose_name='egreso'
        verbose_name_plural = 'egresos'
        order_with_respect_to = 'fecha_pedido'
    
    def __str__(self):
        return f"Egreso #{self.id} - {self.cliente.username}"
   
class Empresa(models.Model):
    
    nombre = models.CharField(max_length=200, null=True, blank=True)
    domicilio = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='empresa'
        verbose_name_plural = 'empresas'
    
    def __str__(self):
        return self.nombre

opcionesConsulta = [
    [0,"Consulta"],
    [1,"Reclamo"],
    [2,"Sugerencia"],
    [3,"Felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField()
    tipoConsulta = models.IntegerField(choices=opcionesConsulta)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre   

