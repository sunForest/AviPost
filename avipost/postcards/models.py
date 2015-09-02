from django.db import models
from django.contrib.auth.models import User


class Postcard(models.Model):
    # didn't use TextField here because Django doesn't check max length for textField?
    message = models.CharField('Message', max_length=140, default="Hello!")
    cover = models.ImageField('Cover', default="placeholder.jpg")
    sender = models.ForeignKey(User)
