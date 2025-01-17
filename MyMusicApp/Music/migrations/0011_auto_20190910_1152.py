# Generated by Django 2.2.2 on 2019-09-10 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0010_auto_20190822_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='artist',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Music.Artist'),
        ),
        migrations.AddField(
            model_name='music',
            name='slug',
            field=models.SlugField(blank=True, max_length=140, null=True, unique=True),
        ),
    ]
