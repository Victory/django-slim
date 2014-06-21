# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import infoorg.validators


class Migration(migrations.Migration):

    dependencies = [
        ('infoorg', '0004_auto_20140621_2344'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformerIpNotes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=140, validators=[infoorg.validators.validate_title])),
                ('note', models.TextField()),
                ('date_added', models.DateTimeField()),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='informer',
            name='ip_notes',
            field=models.ForeignKey(default=None, verbose_name=b'notes about intellectual property rights', to_field='id', to='infoorg.InformerIpNotes'),
            preserve_default=False,
        ),
    ]
