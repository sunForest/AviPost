# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postcards', '0003_auto_20150917_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcard',
            name='latitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postcard',
            name='longitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
