from django.test import TestCase
from .models import Postcard

class PostcardAPITests(TestCase):

    def setUp(self):
        Postcard.objects.get_or_create(content='hello1')
        Postcard.objects.get_or_create(content='hello2')
        self.create_read_url = '/api/v1/postcards/'

    def test_list(self):
        response = self.client.get(self.create_read_url)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'hello1')
        self.assertContains(response, 'hello2')