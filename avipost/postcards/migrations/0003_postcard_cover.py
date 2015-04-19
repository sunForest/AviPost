# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postcards', '0002_auto_20150414_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcard',
            name='cover',
            field=models.ImageField(default=b'images/placeholder.jpg', upload_to=b'', verbose_name=b'Cover'),
            preserve_default=True,
        ),
    ]
