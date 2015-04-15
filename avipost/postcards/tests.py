from django.test import TestCase
from .models import Postcard

class PostcardAPITests(TestCase):

    def setUp(self):
        Postcard.objects.get_or_create(message='hello1')
        Postcard.objects.get_or_create(message='hello2')
        self.create_read_url = '/postcards/'

    def test_list(self):
        response = self.client.get(self.create_read_url)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'hello1')
        self.assertContains(response, 'hello2')