from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from . import forms, models

class HomePageView(generic.TemplateView):
    template_name = 'home.html'


class DestinationCreate(CreateView):
    model = models.Destination
    fields = ['name', 'postal_code', ]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(DestinationCreate, self).form_valid(form)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    model = models.User
    template_name = 'signup.html'
