from django.db import models
from geopy.geocoders import Nominatim


class Location(models.Model):
    postal_code = models.CharField(max_length=12)
    latitude = models.FloatField()
    longitude = models.FloatField()

    geolocator = Nominatim()

    def geocode(self):
        point = self.geolocator.geocode({'country': 'USA',
                                         'postal_code': self.postal_code})
        (self.latitude, self.longitude) = (point.latitude, point.longitude)


class Upload(models.Model):
    source_file = models.FileField(upload_to='documents/%Y/%m/%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location)

    class Meta:
        ordering = ['uploaded_at']


class Destination(models.Model):
    name = models.TextField()
    location = models.ForeignKey(Location)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)


class Traveller(models.Model):
    location = models.ForeignKey(Location)
    email = models.TextField()
    destination = models.ForeignKey(Destination)
    opted_out = models.BooleanField(default=None)
    companions = models.ManyToManyField('Traveller')
    created_at = models.DateTimeField(auto_now_add=True)
