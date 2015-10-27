from django.db import models
from django.contrib.auth.models import User


class Postcard(models.Model):
    # didn't use TextField here because Django doesn't check max length for
    # textField?
    message = models.CharField('Message', max_length=140, default="Hello!")
    cover = models.ImageField('Cover', default="placeholder.jpg")
    sender = models.ForeignKey(User, related_name="sent_by", default=1)
    receiver = models.ForeignKey(User, related_name="received_by", default=1)
    longitude = models.FloatField()
    latitude = models.FloatField()
