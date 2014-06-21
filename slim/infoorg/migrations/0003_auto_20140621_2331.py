# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import infoorg.validators


class Migration(migrations.Migration):

    dependencies = [
        ('infoorg', '0002_informer_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformerFiles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=140, validators=[infoorg.validators.validate_title])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='informer',
            name='files',
            field=models.ForeignKey(default=None, verbose_name=b'files related to the informer', to_field='id', to='infoorg.InformerFiles'),
            preserve_default=False,
        ),
    ]
