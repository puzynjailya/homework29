from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from ads import settings
from categories.models import Category
from users.models import User


class Advertisement(models.Model):
    name = models.CharField(max_length=150,
                            null=True,
                            blank=False,
                            validators=[MinLengthValidator(10, message='Минимальная длина поля 10 символов')])
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                               to_field='id',
                               on_delete=models.CASCADE)
    price = models.IntegerField(blank=False,
                                validators=[MinValueValidator(0, message='Минимальное значение цены 0')])
    description = models.CharField(max_length=3000,
                                   null=True,
                                   blank=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


