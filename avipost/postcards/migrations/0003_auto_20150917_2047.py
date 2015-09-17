# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('postcards', '0002_auto_20150917_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcard',
            name='receiver',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1, related_name='received_by'),
        ),
        migrations.AlterField(
            model_name='postcard',
            name='sender',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1, related_name='sent_by'),
        ),
    ]
