# Generated by Django 3.2.9 on 2022-01-18 13:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_userproflie'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproflie',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='friend_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
