# Generated by Django 3.2.14 on 2022-07-11 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_tipo_producto_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='TIPO_MASCOTA',
            fields=[
                ('id_tipo_mascota', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tipo de Mascota',
                'verbose_name_plural': 'Tipos de Mascotas',
                'db_table': 'TIPO_MASCOTA',
                'ordering': ['id_tipo_mascota'],
            },
        ),
        migrations.AlterField(
            model_name='productos',
            name='tipo_producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.tipo_producto'),
        ),
        migrations.AddField(
            model_name='productos',
            name='tipo_mascota',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.tipo_mascota'),
        ),
    ]
