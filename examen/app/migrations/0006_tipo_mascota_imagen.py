# Generated by Django 4.0.5 on 2022-07-12 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_contacto_alter_productos_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipo_mascota',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='mascotas/'),
        ),
    ]
