# Generated by Django 5.1 on 2024-12-05 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id_inventario', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('id_producto', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('fecha_ingreso', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
                ('id_proveedor', models.IntegerField()),
                ('Notas', models.TextField()),
            ],
        ),
    ]
