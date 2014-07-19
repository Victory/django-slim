from django.db import models

# Create your models here.

from infoorg.validators import (
    validate_title,
    validate_description)


class InformerFiles(models.Model):
    title = models.CharField(
        max_length=140,
        validators=[validate_title])


class InformerLinks(models.Model):
    title = models.CharField(
        max_length=140,
        validators=[validate_title])

    url = models.TextField()


class InformerIpNotes(models.Model):
    title = models.CharField(
        max_length=140,
        validators=[validate_title])
    note = models.TextField()

    date_added = models.DateTimeField()
    last_modified = models.DateTimeField(auto_now_add=True)


class InformerStatusType(models.Model):
    title = models.CharField(
        max_length=140,
        validators=[validate_title])


class Informer(models.Model):
    title = models.CharField(
        max_length=140,
        validators=[validate_title])

    description = models.TextField(
        validators=[validate_description])

    author = models.CharField(
        max_length=140)

    files = models.ForeignKey(
        InformerFiles,
        verbose_name="files related to this informer")

    links = models.ForeignKey(
        InformerLinks,
        verbose_name="links related to this informer")

    ip_notes = models.ForeignKey(
        InformerIpNotes,
        verbose_name="notes about intellectual property rights")

    informer = models.ForeignKey(InformerStatusType, primary_key=True)

    date_added = models.DateTimeField()
    last_modified = models.DateTimeField(auto_now_add=True)


class InfoTip(models.Model):
    subject = models.CharField(
        max_length=140,
        validators=[validate_title])

    message = models.TextField(
        validators=[validate_description])

    sender = models.EmailField()

    def __unicode__(self):
        return unicode(self.subject)
