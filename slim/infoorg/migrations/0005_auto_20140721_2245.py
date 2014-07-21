# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infoorg', '0004_auto_20140721_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informer',
            name='files',
            field=models.ForeignKey(verbose_name=b'files related to this informer', to_field='id', to='infoorg.InformerFiles', null=True),
        ),
    ]
