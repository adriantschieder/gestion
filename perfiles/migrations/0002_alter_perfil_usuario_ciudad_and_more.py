# Generated by Django 4.0 on 2022-02-01 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil_usuario',
            name='ciudad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='perfil_usuario',
            name='direccion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='perfil_usuario',
            name='provincia',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]