import json
from django.test import TestCase
from .models import Postcard


class PostcardAPITests(TestCase):

    def setUp(self):
        Postcard.objects.create(message='hello1')
        Postcard.objects.create(message='hello2')
        self.create_read_url = '/postcards/'

    def test_list(self):
        response = self.client.get(self.create_read_url)
        self.assertEquals(response.status_code, 200)
        postcards = json.loads(response.content)
        self.assertEqual(len(postcards), 2)
        self.assertEqual(postcards[0]['message'], 'hello1')
        self.assertEqual(postcards[1]['message'], 'hello2')
        self.assertRegexpMatches(postcards[0]['cover'], r'images/placeholder.jpg$')
        self.assertRegexpMatches(postcards[1]['cover'], r'images/placeholder.jpg$')
