# Generated by Django 4.2 on 2023-04-17 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_alter_flight_arrival_city_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flight',
            options={'verbose_name': 'Информация о маршруте'},
        ),
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name': 'Информация о пассажире'},
        ),
    ]
