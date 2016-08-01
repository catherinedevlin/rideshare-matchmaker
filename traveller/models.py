from django.db import models
from geopy.geocoders import Nominatim
from datetime import date


class Location(models.Model):
    postal_code = models.CharField(max_length=12)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    geolocator = Nominatim()

    def geocode(self):
        point = self.geolocator.geocode({'country': 'USA',
                                         'postal_code': self.postal_code})
        (self.latitude, self.longitude) = (point.latitude, point.longitude)


ohio_union = Location(postal_code='43210')
ohio_union.save()


class Destination(models.Model):
    name = models.TextField()
    location = models.ForeignKey(Location)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)


pyohio = Destination(name='PyOhio', location=ohio_union, date=date.today())
pyohio.save()


class Upload(models.Model):
    source_file = models.FileField(upload_to='documents/%Y/%m/%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Destination, default=pyohio)

    class Meta:
        ordering = ['uploaded_at']


class Traveller(models.Model):
    location = models.ForeignKey(Location)
    email = models.TextField()
    destination = models.ForeignKey(Destination)
    opted_out = models.BooleanField(default=None)
    companions = models.ManyToManyField('Traveller')
    created_at = models.DateTimeField(auto_now_add=True)
