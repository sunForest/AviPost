import math
import os
import uuid
from io import BytesIO

from PIL import Image

from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage as storage
from django.db import models


def rename_image(instance, filename):
    upload_to = 'media'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4(), ext)
    return os.path.join(upload_to, filename)


class Messenger(models.Model):
    name = models.CharField('Name', max_length=50)
    portrait = models.ImageField('Portrait')
    description = models.TextField('Description')


class Postcard(models.Model):
    message = models.CharField('Message', max_length=140, default="Hello!")
    image_height = models.PositiveIntegerField()
    image_width = models.PositiveIntegerField()
    cover = models.ImageField(
        'Cover',
        upload_to=rename_image,
        height_field='image_height',
        width_field='image_width')
    cover_thumbnail_small = models.ImageField(editable=False)
    cover_thumbnail_medium = models.ImageField(editable=False)
    cover_thumbnail_large = models.ImageField(editable=False)
    longitude = models.FloatField()
    latitude = models.FloatField()
    sender = models.ForeignKey(User, related_name="sent_by", default=1)
    receiver = models.ForeignKey(User, related_name="received_by", default=1)
    messenger = models.ForeignKey(Messenger, related_name="delivered_by")

    def save(self, *args, **kwargs):
        """
        Make and save the thumbnail for the photo here.
        """
        super(Postcard, self).save(*args, **kwargs)
        base_width = 30
        self.make_thumbnail(base_width, self.cover_thumbnail_small)
        self.make_thumbnail(base_width * 2, self.cover_thumbnail_medium)
        self.make_thumbnail(base_width * 3, self.cover_thumbnail_large)

    def make_thumbnail(self, width, field_name):
        height = math.ceil(width * self.cover.height / self.cover.width)
        thumb_size = width, height
        fh = storage.open(self.cover.name, 'rb')
        image = Image.open(fh)
        image.thumbnail(thumb_size, Image.ANTIALIAS)
        fh.close()

        # Path to save to, name, and extension
        thumb_name, _ = os.path.splitext(self.cover.name)
        thumb_filename = '{0}_thumb_w{1}.jpg'.format(thumb_name, width)
        # Save thumbnail to in-memory file as StringIO
        temp_thumb = BytesIO()
        image.save(temp_thumb, 'JPEG')
        temp_thumb.seek(0)

        # Load a ContentFile into the thumbnail field so it gets saved
        field_name.save(
            thumb_filename,
            ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()
