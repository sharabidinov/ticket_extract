from django.db import models


# Create your models here.
class Ticket(models.Model):
    class Meta:
        verbose_name = 'Информация о пассажире'
        verbose_name_plural = 'Информация о пассажирах'

    first_name = models.CharField(
        max_length=128,
        verbose_name='Имя',
    )
    last_name = models.CharField(
        max_length=128,
        verbose_name='Фамилия',
    )
    pnr_number = models.CharField(
        max_length=6,
        verbose_name='Номер PNR',
        unique=True
    )
    rl_number = models.CharField(
        max_length=6,
        verbose_name='Номер RL',
        unique=True
    )
    ticket_number = models.CharField(
        max_length=14,
        verbose_name='Номер билета',
        unique=True
    )
    document_number = models.CharField(
        max_length=9,
        verbose_name='Номер документа',
        unique=True
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата оформления',
    )

    def __str__(self):
        return self.first_name + " " + self.last_name


class Flight(models.Model):
    class Meta:
        verbose_name = 'Информация о маршруте'
        verbose_name_plural = 'Информация о маршрутах'

    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        null=True,
        related_name='Flights',
        verbose_name='Пользователь',
    )
    departure_time = models.DateTimeField(
        verbose_name='Время вылета',
    )
    departure_city = models.CharField(
        max_length=128,
        verbose_name='Город вылета',
    )
    departure_airport_code = models.CharField(
        max_length=10,
        verbose_name='Код аэропорта вылета',
    )
    departure_location = models.CharField(
        max_length=128,
        verbose_name='Аэропорт вылета',
    )
    departure_terminal = models.CharField(
        max_length=10,
        verbose_name='Терминал аэропорта вылета',
    )
    arrival_time = models.DateTimeField(
        verbose_name='Время прилёта',
    )
    arrival_city = models.CharField(
        max_length=128,
        verbose_name='Город прилёта'
    )
    arrival_airport_code = models.CharField(
        max_length=10,
        verbose_name='Код аэропорта прилёта'
    )
    arrival_location = models.CharField(
        max_length=128,
        verbose_name='Аэропорт прилёта'
    )
    arrival_terminal = models.CharField(
        max_length=10,
        verbose_name='Терминал аэропорта прилёта'
    )
    aircraft_type = models.CharField(
        max_length=128,
        verbose_name='Рейс',
    )
    class_type = models.CharField(
        max_length=20,
        verbose_name='Класс'
    )
    luggage = models.CharField(
        max_length=10,
        verbose_name='Багаж'
    )

    def __str__(self):
        return self.departure_city + '-' + self.arrival_city + ' ' + self.ticket.__str__()
