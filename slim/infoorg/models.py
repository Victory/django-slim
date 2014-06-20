from django.db import models

# Create your models here.

from infoorg.validators import *

class Informer(models.Model):
    title = models.CharField(
        max_length=140,
        validators=[validate_title])
    description = models.TextField(
        validators=[validate_description])
    author = models.CharField(
        max_length=140)
