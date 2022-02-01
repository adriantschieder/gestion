# Generated by Django 4.0 on 2022-02-01 17:07

import builtins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil_Usuario',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=builtins.id, serialize=False, to='auth.user')),
                ('direccion', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=100)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('avatar', models.ImageField(blank=True, default='avatar.png', null=True, upload_to='avatar')),
            ],
        ),
    ]
