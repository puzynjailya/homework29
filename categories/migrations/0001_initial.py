# Generated by Django 4.0.1 on 2022-08-11 20:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('slug', models.CharField(db_index=True, default='category_<django.db.models.fields.AutoField>', max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(5, message='Минимальная длина 5 символов')])),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
    ]
