# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postcards', '0006_postcard_messenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcard',
            name='messenger',
            field=models.ForeignKey(to='postcards.Messenger', related_name='delivered_by', default=1),
        ),
    ]
