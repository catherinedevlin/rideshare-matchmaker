from django.forms import ModelForm
from .models import Destination

class DestinationForm(ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'postal_code', ]
