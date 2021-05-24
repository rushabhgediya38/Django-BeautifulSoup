from django.db import models
from structured_data import *


# Create your models here.


class sData(models.Model):
    title = models.CharField(max_length=400, blank=True, null=True)
    author = models.CharField(max_length=400, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    SITE_URL = models.URLField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

