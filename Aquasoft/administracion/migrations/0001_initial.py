# Generated by Django 5.0.3 on 2024-05-03 23:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(default='@gmail.com', max_length=254)),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('telefono', models.CharField(blank=True, max_length=200, null=True)),
                ('direccion', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('domicilio', models.CharField(blank=True, max_length=200, null=True)),
                ('telefono', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'empresa',
                'verbose_name_plural': 'empresas',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('descripcion', models.CharField(max_length=200, null=True, unique=True)),
                ('detalle', models.CharField(blank=True, max_length=1000, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos')),
                ('costo', models.DecimalField(decimal_places=2, max_digits=13, null=True)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=15, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
            },
        ),
        migrations.CreateModel(
            name='Egreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('pagado', models.CharField(choices=[('si', 'Sí'), ('no', 'No')], default='no', max_length=2)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('ticket', models.BooleanField(default=True)),
                ('desglosar', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cliente', to='administracion.cliente')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='producto', to='administracion.producto')),
            ],
            options={
                'verbose_name': 'egreso',
                'verbose_name_plural': 'egresos',
                'order_with_respect_to': 'fecha_pedido',
            },
        ),
    ]
