from django.core.validators import MinLengthValidator
from django.db import models


class Category(models.Model):
    id = models.AutoField(editable=False, unique=True, primary_key=True, auto_created=True)
    name = models.CharField(max_length=50, null=True, blank=False)
    slug = models.CharField(max_length=10,
                            validators=[MinLengthValidator(5, message="Минимальная длина 5 символов")],
                            unique=True,
                            db_index=True,
                            null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

