# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postcards', '0010_postcard_cover_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcard',
            old_name='cover_thumbnail',
            new_name='cover_thumbnail_large',
        ),
        migrations.AddField(
            model_name='postcard',
            name='cover_thumbnail_medium',
            field=models.ImageField(upload_to='', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postcard',
            name='cover_thumbnail_small',
            field=models.ImageField(upload_to='', default=''),
            preserve_default=False,
        ),
    ]
