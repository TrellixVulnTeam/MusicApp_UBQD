# Generated by Django 2.2.2 on 2019-09-14 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment_commentreply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='commentreply',
            name='message',
            field=models.TextField(max_length=500),
        ),
    ]
