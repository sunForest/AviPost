from django.db import models

class Postcard(models.Model):
    # didn't use TextField here because Django doesn't check max length for textField?
    message = models.CharField('Message', max_length=140, default="Hello!")
    cover = models.ImageField('Cover')
    sender = models.CharField('Sender', max_length=20, default="demo")
