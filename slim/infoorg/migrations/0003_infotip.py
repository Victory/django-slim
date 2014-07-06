# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import infoorg.validators


class Migration(migrations.Migration):

    dependencies = [
        ('infoorg', '0002_auto_20140622_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoTip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=140, validators=[infoorg.validators.validate_title])),
                ('message', models.TextField(validators=[infoorg.validators.validate_description])),
                ('sender', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
