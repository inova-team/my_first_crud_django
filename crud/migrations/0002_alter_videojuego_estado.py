# Generated by Django 3.2.19 on 2023-06-29 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videojuego',
            name='estado',
            field=models.IntegerField(default=1),
        ),
    ]
