# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postcards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcard',
            name='content',
        ),
        migrations.AddField(
            model_name='postcard',
            name='message',
            field=models.TextField(default=b'Hello!', verbose_name=b'Message'),
            preserve_default=True,
        ),
    ]
