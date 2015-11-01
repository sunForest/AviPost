from django.db import models
from django.contrib.auth.models import User


class Messenger(models.Model):
    name = models.CharField('Name', max_length=50)
    portrait = models.ImageField('Portrait')
    description = models.TextField('Description')


class Postcard(models.Model):
    message = models.CharField('Message', max_length=140, default="Hello!")
    cover = models.ImageField('Cover')
    longitude = models.FloatField()
    latitude = models.FloatField()
    sender = models.ForeignKey(User, related_name="sent_by", default=1)
    receiver = models.ForeignKey(User, related_name="received_by", default=1)
    messenger = models.ForeignKey(Messenger, related_name="delivered_by")
