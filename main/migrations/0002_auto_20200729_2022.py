# Generated by Django 3.0.3 on 2020-07-29 14:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='reserved',
            field=models.ManyToManyField(blank=True, default=[0], related_name='event_reservations', to=settings.AUTH_USER_MODEL),
        ),
    ]
