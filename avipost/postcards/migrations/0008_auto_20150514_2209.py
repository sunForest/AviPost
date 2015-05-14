# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postcards', '0007_postcard_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcard',
            name='cover',
            field=models.ImageField(default=b'placeholder.jpg', upload_to=b'', verbose_name=b'Cover'),
            preserve_default=True,
        ),
    ]
