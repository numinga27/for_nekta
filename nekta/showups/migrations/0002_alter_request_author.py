# Generated by Django 3.2.7 on 2023-05-19 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
