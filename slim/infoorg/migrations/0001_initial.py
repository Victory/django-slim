# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import infoorg.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Informer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=140, validators=[infoorg.validators.validate_title])),
                ('description', models.TextField(validators=[infoorg.validators.validate_description])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
