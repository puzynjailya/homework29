# Generated by Django 4.0.1 on 2022-08-02 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selections', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='selection',
            options={'verbose_name': 'Выборка', 'verbose_name_plural': 'Выборки'},
        ),
    ]