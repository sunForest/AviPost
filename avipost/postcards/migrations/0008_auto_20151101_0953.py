# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postcards', '0007_auto_20151101_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcard',
            name='messenger',
            field=models.ForeignKey(related_name='delivered_by', to='postcards.Messenger'),
        ),
    ]
