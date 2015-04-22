import json
import os
from django.test import TestCase
from django.conf import settings
from postcards.models import Postcard



class PostcardAPITests(TestCase):

    def setUp(self):
        Postcard.objects.create(message='hello1')
        Postcard.objects.create(message='hello2')
        self.create_read_url = '/postcards/'
        slug = Postcard.objects.all()[0].id
        self.detail_url = '/postcards/{}/'.format(slug)

    def test_list(self):
        response = self.client.get(self.create_read_url)
        self.assertEquals(response.status_code, 200)
        postcards = json.loads(response.content)
        self.assertEqual(len(postcards), 2)

    def test_detail_should_show_all_the_attributes(self):
        response =  self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '"message":"hello1"')
        self.assertContains(response, '/media/placeholder.jpg')
        self.assertContains(response, '"sender":"demo"')

    def test_create(self):
        post = {'message': 'A short and warm greeting.'}
        response = self.client.post(self.create_read_url, post)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Postcard.objects.count(), 3)

    def test_create_should_fail_for_long_messages(self):
        post = {'message': 'This is definitely too long. '*10}
        response = self.client.post(self.create_read_url, post)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Postcard.objects.count(), 2)

    def test_delete(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Postcard.objects.count(), 1)


class FileUploadTest(TestCase):

    def setUp(self):
        self.create_url = '/postcards/'

    def tearDown(self):
        # delete the uploaded image
        image_path = os.path.join(settings.BASE_DIR, 'media', 'test_image.jpg')
        os.remove(image_path)

    def test_file_uploading(self):
        with open('postcards/tests/test_image.jpg') as fp:
            post = {'message': 'test image uploading',
                'cover': fp}
            response = self.client.post(self.create_url, post)
            self.assertEqual(response.status_code, 201)
