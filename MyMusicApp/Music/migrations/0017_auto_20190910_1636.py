# Generated by Django 2.2.2 on 2019-09-10 15:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0016_auto_20190910_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1980), django.core.validators.MaxValueValidator(2050)]),
        ),
    ]
