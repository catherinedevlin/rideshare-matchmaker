# -*- coding: utf-8 -*-

from django import forms


class TravellerDocumentForm(forms.Form):

    source_file = forms.FileField(
        label='Choose file of traveller data'
    )
