# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from . import forms, models



def list(request):
    if request.method == 'POST':
        form = forms.TravellerDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = models.Upload(source_file=request.FILES['source_file'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = forms.TravellerDocumentForm()  # A empty, unbound form

    uploads = models.Upload.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'list.html',
        {'documents': uploads, 'form': form}
    )
