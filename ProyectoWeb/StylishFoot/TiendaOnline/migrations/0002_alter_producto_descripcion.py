# Generated by Django 4.0.4 on 2022-06-07 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaOnline', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=100, verbose_name='Descripcion'),
        ),
    ]
