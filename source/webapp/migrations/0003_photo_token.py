# Generated by Django 4.1.1 on 2022-09-24 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_album_isprivate_alter_photo_isprivate'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='token',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]