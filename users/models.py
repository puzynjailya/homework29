from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=200, blank=False)
    lat = models.DecimalField(max_digits=8, decimal_places=6, default=0.0)
    lng = models.DecimalField(max_digits=8, decimal_places=6, default=0.0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Локации'


class User(AbstractUser):
    ROLES = [
        ('admin', 'Администратор ОПГ'),
        ('member', 'Участник ОПГ'),
        ('moderator', 'Смотрящий за ОПГ'),
    ]

    role = models.CharField(max_length=9, choices=ROLES, blank=False, default='member')
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    location = models.ManyToManyField(Location)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
