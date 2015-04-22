# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postcards', '0006_auto_20150420_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcard',
            name='sender',
            field=models.CharField(default=b'demo', max_length=20, verbose_name=b'Sender'),
            preserve_default=True,
        ),
    ]
