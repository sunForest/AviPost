from django.db import models

class Postcard(models.Model):
    message = models.TextField('Message', default="Hello!")