# Generated by Django 2.0 on 2021-02-25 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAnimalPerformance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='precio_costo',
            field=models.FloatField(default=float),
            preserve_default=False,
        ),
    ]
