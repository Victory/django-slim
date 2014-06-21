from django.db import models

# Create your models here.

from infoorg.validators import *


class InformerFiles(models.Model):
    title = models.CharField(
        max_length=140,
        validators=[validate_title])


class InformerLinks(models.Model):
    title = models.CharField(
        max_length=140,
        validators=[validate_title])
    url = models.TextField()


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
