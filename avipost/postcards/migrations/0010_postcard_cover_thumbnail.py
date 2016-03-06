# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postcards', '0009_auto_20160304_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcard',
            name='cover_thumbnail',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
