# Generated by Django 2.2.2 on 2019-09-11 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0030_music_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
