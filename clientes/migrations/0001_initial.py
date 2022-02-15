# Generated by Django 4.0 on 2022-02-15 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(blank=True, max_length=50, null=True)),
                ('condicion_iva', models.CharField(max_length=30)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('domicilio', models.CharField(max_length=100)),
                ('mail', models.EmailField(blank=True, max_length=254, null=True)),
                ('cuit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Maquinarias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('propietario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.clientes')),
            ],
        ),
        migrations.CreateModel(
            name='Arreglo_Maquinarias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_arreglo', models.DateField(null=True)),
                ('arreglo', models.CharField(max_length=200)),
                ('maquinaria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.maquinarias')),
            ],
        ),
    ]
