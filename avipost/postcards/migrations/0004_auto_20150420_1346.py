# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postcards', '0003_postcard_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcard',
            name='message',
            field=models.TextField(default=b'Hello!', max_length=10, verbose_name=b'Message'),
            preserve_default=True,
        ),
    ]
