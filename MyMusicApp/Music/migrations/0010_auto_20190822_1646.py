# Generated by Django 2.2.2 on 2019-08-22 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0009_auto_20190822_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='year',
            field=models.CharField(max_length=4, unique=True),
        ),
    ]
