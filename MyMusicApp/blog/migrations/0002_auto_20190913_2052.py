# Generated by Django 2.2.2 on 2019-09-13 19:52

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=blog.models.image_upload),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=40, null=True, unique=True),
        ),
    ]
