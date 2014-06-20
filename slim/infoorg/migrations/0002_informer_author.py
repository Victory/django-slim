# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infoorg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='informer',
            name='author',
            field=models.CharField(default='author', max_length=140),
            preserve_default=False,
        ),
    ]
