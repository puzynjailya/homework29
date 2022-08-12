import re

from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date
from rest_framework.exceptions import ValidationError


class Location(models.Model):
    name = models.CharField(max_length=200, blank=False)
    lat = models.DecimalField(max_digits=8, decimal_places=6, default=0.0)
    lng = models.DecimalField(max_digits=8, decimal_places=6, default=0.0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Локации'


def age_validation(value: date):
    if date.today().year - value.year < 9:
        raise ValidationError(f"Возраст пользователя меньше 9 лет. Ай-ай-ай")
    if date.today().year - value.year == 9:
        if date.today().month >= value.month:
            if date.today().day < value.day:
                raise ValidationError(f"Возраст пользователя меньше 9 лет. Ай-ай-ай")
        else:
            raise ValidationError(f"Возраст пользователя меньше 9 лет. Ай-ай-ай")


def email_validation(value: str):
    email_matches_pattern = re.fullmatch(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+(@rambler.ru)", value)
    if email_matches_pattern is not None:
        raise ValidationError(f"Почтовый адрес: {value} использует запрещенный домен")


class User(AbstractUser):
    ROLES = [
        ('admin', 'Администратор ОПГ'),
        ('member', 'Участник ОПГ'),
        ('moderator', 'Смотрящий за ОПГ'),
    ]

    role = models.CharField(max_length=9,
                            choices=ROLES,
                            blank=False,
                            default='member')
    age = models.PositiveSmallIntegerField(blank=True,
                                           null=True)
    location = models.ManyToManyField(Location)
    birth_date = models.DateField(validators=[age_validation],
                                  default=date(1930, 1, 1))
    email = models.EmailField(unique=True,
                              blank=False,
                              null=False,
                              validators=[email_validation])

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
