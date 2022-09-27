# Generated by Django 4.0.6 on 2022-07-18 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaOnline', '0004_carrito'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleCarrito',
            fields=[
                ('idDetalle', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Detalle')),
                ('idProd', models.IntegerField(verbose_name='Id del producto')),
                ('idclie', models.IntegerField(verbose_name='Id del Cliente')),
                ('nombrePo', models.CharField(max_length=100, verbose_name='Nombre del Producto')),
            ],
        ),
        migrations.AlterField(
            model_name='cliente',
            name='correo',
            field=models.CharField(max_length=40, unique=True, verbose_name='Correo Cliente'),
        ),
    ]