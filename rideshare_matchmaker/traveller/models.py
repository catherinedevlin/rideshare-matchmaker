from django.db import models

class Location(models.Model):
    postal_code = models.CharField()
    latitude = models.FloadField()
    longitude = models.FloadField()


class Destination(models.Model):
    name = models.TextField()
    location = models.ForeignKey(Location)
    date = models.DateField()


class Traveller(models.Model):
    location = models.ForeignKey(Location)
    email = models.TextField()
    destination = models.ForeignKey(Destination)
    opted_out = models.BooleanField(default=None)
    companions = models.ManyToManyField(Traveller)
