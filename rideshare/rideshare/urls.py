"""rideshare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

from riders.views import HomePageView, DestinationCreate, SignUpView

urlpatterns = [
    url(r'^$', HomePageView.as_view()),
    url(r'^create_destination/', login_required(DestinationCreate.as_view())),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html', }),
    url(r'^accounts/signup/$', SignUpView.as_view(), {'template_name': 'signup.html', }),
    url(r'^admin/', admin.site.urls),
]
