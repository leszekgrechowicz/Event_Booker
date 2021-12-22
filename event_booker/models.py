from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import datetime


class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    places = models.SmallIntegerField()
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    age_restriction = models.BooleanField()

    def __str__(self):
        return f'{self.name}'


class Customer(models.Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=180)
    email = models.EmailField()
    berth_year = models.IntegerField(validators=[MinValueValidator(1500),
                                                 MaxValueValidator(datetime.datetime.now().year)])
    is_checked = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    invited = models.BooleanField(default=False)
    uuid = models.UUIDField()

    event = models.ForeignKey(Event, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} {self.surname}'


class EventImage(models.Model):
    scr = models.ImageField()

    event = models.ForeignKey(Event, on_delete=models.PROTECT)

