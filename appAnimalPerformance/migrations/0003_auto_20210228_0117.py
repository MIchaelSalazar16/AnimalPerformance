# Generated by Django 2.0 on 2021-02-28 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appAnimalPerformance', '0002_animal_precio_costo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rendimiento',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='rendimiento',
            name='hora',
        ),
    ]
