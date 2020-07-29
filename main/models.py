from django.db import models
from django.conf import settings

# Create your models here.
class Event(models.Model):
    img = models.ImageField(upload_to=None)
    name = models.CharField(max_length=128)
    venue = models.CharField(max_length=128)
    time = models.TimeField()
    date = models.DateField()
    reserved = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="event_reservations")

    def __str__(self):
        return self.name