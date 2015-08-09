from django.db import models
from django.contrib.auth.models import User

class OAuthUser(models.Model):
    user = models.OneToOneField(User)
    oauth_provider = models.CharField('OAuth Provider', max_length=50)

