# -*- coding: utf-8 -*-
from django.db import models
from main import translate

# Create your models here.


class Translate(models.Model):
    """Tranlate Text"""
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'Название')
    titleru = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'Название(rus)')
    body = models.TextField(verbose_name='Оригинал', null=True, blank=True)
    bodyru = models.TextField(verbose_name='Перевод', null=True, blank=True)

    def __unicode__(self):
        return self.title

    def clean(self):
        if (self.title is not None) and (self.titleru == ''):
            self.titleru = translate(self.title)
        if (self.body is not None) and (self.bodyru == ''):
            self.bodyru = translate(self.body)
