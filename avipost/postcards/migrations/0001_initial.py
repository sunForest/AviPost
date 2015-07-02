# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postcard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(default=b'Hello!', max_length=140, verbose_name=b'Message')),
                ('cover', models.ImageField(default=b'placeholder.jpg', upload_to=b'', verbose_name=b'Cover')),
                ('sender', models.CharField(default=b'demo', max_length=20, verbose_name=b'Sender')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
