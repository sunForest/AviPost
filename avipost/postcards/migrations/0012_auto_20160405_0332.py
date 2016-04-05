# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import postcards.models


class Migration(migrations.Migration):

    dependencies = [
        ('postcards', '0011_auto_20160304_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcard',
            name='cover',
            field=models.ImageField(upload_to=postcards.models.rename_image, height_field='image_height', width_field='image_width', verbose_name='Cover'),
        ),
        migrations.AlterField(
            model_name='postcard',
            name='cover_thumbnail_large',
            field=models.ImageField(upload_to='', editable=False),
        ),
        migrations.AlterField(
            model_name='postcard',
            name='cover_thumbnail_medium',
            field=models.ImageField(upload_to='', editable=False),
        ),
        migrations.AlterField(
            model_name='postcard',
            name='cover_thumbnail_small',
            field=models.ImageField(upload_to='', editable=False),
        ),
    ]
