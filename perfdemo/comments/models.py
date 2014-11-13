# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

class Comment(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['id']
