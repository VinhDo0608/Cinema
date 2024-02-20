from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255)
    discount = models.SmallIntegerField()
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()