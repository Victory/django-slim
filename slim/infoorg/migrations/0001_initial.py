# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import infoorg.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InformerStatusType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=140, validators=[infoorg.validators.validate_title])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
        migrations.CreateModel(
            name='Informer',
            fields=[
                ('title', models.CharField(max_length=140, validators=[infoorg.validators.validate_title])),
                ('description', models.TextField(validators=[infoorg.validators.validate_description])),
                ('author', models.CharField(max_length=140)),
                ('files', models.ForeignKey(to='infoorg.InformerFiles', to_field='id', verbose_name=b'files related to this informer')),
                ('links', models.ForeignKey(to='infoorg.InformerLinks', to_field='id', verbose_name=b'links related to this informer')),
                ('ip_notes', models.ForeignKey(to='infoorg.InformerIpNotes', to_field='id', verbose_name=b'notes about intellectual property rights')),
                ('informer', models.ForeignKey(primary_key=True, to_field='id', serialize=False, to='infoorg.InformerStatusType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
