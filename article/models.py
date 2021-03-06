#_*_coding:utf8_*_
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100) #博客目录
    category = models.CharField(max_length = 50,blank = True) #博客标签
    date_time = models.DateTimeField(auto_now_add = True) #博客日期
    content = models.TextField(blank = True,null = True) #博客正文

    #获取 URL 并转换成 url 的表示格式
    def get_absolute_url(self):
        path = reverse('detail',kwargs={'id':self.id})
        return 'http://127.0.0.1:8000%s' %path

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']


