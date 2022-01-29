# Generated by Django 3.2.10 on 2022-01-28 23:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20220128_1956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='texto',
            new_name='cuerpo',
        ),
        migrations.RemoveField(
            model_name='post',
            name='estatus',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AddField(
            model_name='post',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
