from django.test import TestCase
from django.http import HttpRequest
from django.core.urlresolvers import resolve
from riders.views import HomePageView
from django.test.utils import setup_test_environment
from django.test import Client


class HomePageTest(TestCase):

    def setUp(self):
        setup_test_environment()
        self.client = Client()

    def test_homepage_resolves(self):
        found = resolve('/')
        self.assertEqual(found.view_name.split('.')[-1], HomePageView.__name__)

    def test_homepage_contents(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.content.startswith(b'<html>'))
