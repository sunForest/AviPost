# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postcards', '0004_auto_20151027_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messenger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('portrait', models.ImageField(verbose_name='Portrait', upload_to='')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.AlterField(
            model_name='postcard',
            name='cover',
            field=models.ImageField(verbose_name='Cover', upload_to=''),
        ),
    ]
