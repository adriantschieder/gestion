# Generated by Django 3.2.10 on 2022-01-27 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fecha_subida',
            field=models.DateTimeField(auto_now=True),
        ),
    ]