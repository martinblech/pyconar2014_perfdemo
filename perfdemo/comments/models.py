# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

class Comment(models.Model):
    body = models.CharField(max_length=250)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    tags = models.ManyToManyField(Tag)
