# Generated by Django 2.2.6 on 2019-10-14 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20191012_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='display_comment',
            field=models.BooleanField(default=True),
        ),
    ]