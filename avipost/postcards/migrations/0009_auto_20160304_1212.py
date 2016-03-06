# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postcards', '0008_auto_20151101_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcard',
            name='image_height',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postcard',
            name='image_width',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postcard',
            name='cover',
            field=models.ImageField(height_field='image_height', width_field='image_width', upload_to='', verbose_name='Cover'),
        ),
    ]
