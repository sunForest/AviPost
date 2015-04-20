from django.db import models

class Postcard(models.Model):
    message = models.CharField('Message', max_length=140, default="Hello!")
    cover = models.ImageField('Cover', default="images/placeholder.jpg")
