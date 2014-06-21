# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import infoorg.validators


class Migration(migrations.Migration):

    dependencies = [
        ('infoorg', '0003_auto_20140621_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformerLinks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=140, validators=[infoorg.validators.validate_title])),
                ('url', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='informer',
            name='links',
            field=models.ForeignKey(default=None, verbose_name=b'links related to this informer', to_field='id', to='infoorg.InformerLinks'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='informer',
            name='files',
            field=models.ForeignKey(to='infoorg.InformerFiles', to_field='id', verbose_name=b'files related to this informer'),
        ),
    ]
