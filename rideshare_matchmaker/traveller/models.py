from django.db import models
from geopy.geocoders import Nominatim


class Location(models.Model):
    postal_code = models.CharField()
    latitude = models.FloadField()
    longitude = models.FloadField()

    geolocator = Nominatim()

    class geocode(self):
        point = self.geolocator.geocode({'country': 'USA',
                                         'postal_code': self.postal_code})
        (self.latitude, self.longitude) = (point.latitude, point.longitude)


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
