# Generated by Django 2.2.2 on 2019-09-10 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0019_playlist_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='album',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Music.Album'),
        ),
    ]
