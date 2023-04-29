# Generated by Django 4.2 on 2023-04-15 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('pnr_number', models.CharField(max_length=6)),
                ('rl_number', models.CharField(max_length=6)),
                ('ticket_number', models.CharField(max_length=14)),
                ('document_number', models.CharField(max_length=9)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_time', models.DateTimeField()),
                ('departure_city', models.CharField(max_length=128)),
                ('departure_city_code', models.CharField(max_length=10)),
                ('departure_location', models.CharField(max_length=128)),
                ('departure_terminal', models.CharField(max_length=10)),
                ('arrival_time', models.DateTimeField()),
                ('arrival_city', models.CharField(max_length=128)),
                ('arrival_city_code', models.CharField(max_length=10)),
                ('arrival_location', models.CharField(max_length=128)),
                ('arrival_terminal', models.CharField(max_length=10)),
                ('flight', models.CharField(max_length=128)),
                ('class_type', models.CharField(max_length=20)),
                ('luggage', models.CharField(max_length=10)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Flights', to='ticket.ticket')),
            ],
        ),
    ]