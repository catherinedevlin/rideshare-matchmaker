from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User

# Create your models here.

DEFAULT_CAMPAIGN_DURATION_DAYS = 120

def default_days_from_now():
    return datetime.today().date() + timedelta(days=DEFAULT_CAMPAIGN_DURATION_DAYS)


class Destination(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=12)
    delete_date = models.DateField(default=default_days_from_now)
    created_at = models.DateTimeField(auto_now_add=True)
