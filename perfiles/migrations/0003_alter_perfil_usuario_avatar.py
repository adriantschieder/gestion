# Generated by Django 3.2.10 on 2022-02-02 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0002_alter_perfil_usuario_ciudad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil_usuario',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar/avatar.png', null=True, upload_to='avatar'),
        ),
    ]
