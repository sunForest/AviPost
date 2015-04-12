from django.db import models

class Postcard(models.Model):
    content = models.TextField('Content')
