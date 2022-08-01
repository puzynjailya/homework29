from django.contrib.auth import get_user_model
from django.db import models

from advertisements.models import Advertisement

User = get_user_model()


class Selection(models.Model):
    items = models.ManyToManyField(Advertisement)
    name = models.CharField(max_length=25)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=False)

    class Meta:
        verbose_name = "Выборка"
        verbose_name_plural = "Выборки"
