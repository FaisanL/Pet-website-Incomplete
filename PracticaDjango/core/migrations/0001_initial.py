# Generated by Django 4.0.4 on 2022-06-13 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('rutcliente', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='rut del cliente')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre completo del cliente')),
                ('correo', models.CharField(max_length=50, verbose_name='correo del cliente')),
                ('telefono', models.IntegerField(verbose_name='telefono del cliente')),
                ('direccion', models.CharField(max_length=50, verbose_name='direccion del cliente')),
            ],
        ),
    ]
