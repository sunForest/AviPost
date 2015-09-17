# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('postcards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcard',
            name='receiver',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1, related_name='received_by'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postcard',
            name='sender',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='sent_by'),
        ),
    ]
