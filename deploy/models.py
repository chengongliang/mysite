#coding:utf8
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Host(models.Model):
    name = models.CharField(max_length=64,unique=True)
    ip_addr = models.GenericIPAddressField(unique=True)
    host_groups = models.ManyToManyField('HostGroup',blank=True)
    project = models.ManyToManyField('Project',blank=True)
    memo = models.TextField(u"备注",blank=True,null=True)

    def __unicode__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(u'项目名称',max_length=64,unique=True)
    deploy_dir = models.CharField(u'部署目录',max_length=64,unique=True)
    tpye_choices = (
        ('webuser','webuser'),
        ('wwwroot','wwwroot')
    )
    Type = models.CharField(u'项目类型',max_length=64,choices=tpye_choices)
    memo = models.TextField(u"备注",blank=True,null=True)

    def __unicode__(self):
        return self.name

class HostGroup(models.Model):
    name =  models.CharField(max_length=64,unique=True)
    memo = models.TextField(u"备注",blank=True,null=True)

    def __unicode__(self):
        return self.name
