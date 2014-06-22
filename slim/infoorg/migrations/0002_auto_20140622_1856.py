# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('infoorg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='informer',
            name='date_added',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='informer',
            name='last_modified',
            field=models.DateTimeField(default=datetime.date(2014, 6, 22), auto_now_add=True),
            preserve_default=False,
        ),
    ]
