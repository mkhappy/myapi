# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class SensMod(models.Model):
    """ 敏感词数据表 """
    content = models.CharField(max_length=128, null=False, verbose_name=u'请求消息')
    type = models.IntegerField(null=False, verbose_name=u'消息类型')
    message = models.CharField(max_length=128, null=True, verbose_name=u'返回消息')
    sensitive = models.CharField(max_length=128, null=True, verbose_name=u'敏感指数')
    nonsensitive = models.CharField(max_length=128, null=True, verbose_name=u'非敏感指数')
    codedesc = models.CharField(max_length=128, null=True, verbose_name=u'消息描述')
    ip = models.GenericIPAddressField(protocol='IPv4', null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    class Meta:
        verbose_name = "sensitive content detection"
