# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infoorg', '0003_infotip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='informer',
            old_name='informer',
            new_name='status',
        ),
        migrations.AlterField(
            model_name='informer',
            name='links',
            field=models.ForeignKey(verbose_name=b'links related to this informer', to_field='id', to='infoorg.InformerLinks', null=True),
        ),
        migrations.AlterField(
            model_name='informer',
            name='ip_notes',
            field=models.ForeignKey(verbose_name=b'notes about intellectual property rights', to_field='id', to='infoorg.InformerIpNotes', null=True),
        ),
    ]
