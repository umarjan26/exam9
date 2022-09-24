# Generated by Django 4.1.1 on 2022-09-24 14:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0003_photo_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='selected',
            field=models.ManyToManyField(related_name='selected_albums', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='photo',
            name='selected',
            field=models.ManyToManyField(related_name='selected_photos', to=settings.AUTH_USER_MODEL),
        ),
    ]
