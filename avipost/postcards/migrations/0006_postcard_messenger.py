# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postcards', '0005_auto_20151101_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcard',
            name='messenger',
            field=models.ForeignKey(related_name='delivered_by', default=1, to='postcards.Messenger'),
            preserve_default=False,
        ),
    ]
