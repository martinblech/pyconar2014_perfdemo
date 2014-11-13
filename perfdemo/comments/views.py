# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView

from .models import Comment


class CommentListView(ListView):
    queryset = Comment.objects.all()
    #queryset = Comment.objects.all().defer('body')
    #queryset = Comment.objects.all().defer('body').select_related('author')
    #queryset = Comment.objects.all().defer('body').select_related('author').prefetch_related('tags')
