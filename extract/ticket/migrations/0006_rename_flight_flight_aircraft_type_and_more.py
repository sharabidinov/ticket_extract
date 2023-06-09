# Generated by Django 4.2 on 2023-04-23 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_rename_arrival_city_code_flight_arrival_airport_code_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight',
            old_name='flight',
            new_name='aircraft_type',
        ),
        migrations.AlterField(
            model_name='flight',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Flights', to='ticket.ticket', verbose_name='Пользователь'),
        ),
    ]
