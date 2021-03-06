#_*_ coding:utf8 _*_
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404

# Create your views here.
def home(request):
    post_list = Article.objects.all() #获取全部Article对象
    return render(request,'home.html',{'post_list':post_list})
    #return HttpResponse('Hello world,Django')

def detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request,'post.html',{'post':post})

def test(request):
    return render(request, 'home.html', {'current_time': datetime.now()})

def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoseNotExist:
        raise Http404
    return render(request,'archives.html',{'post_list':post_list,
                                          'error':False})
def about_me(request) :
    return render(request, 'aboutme.html')

def search_tag(request, tag) :
    try:
        post_list = Article.objects.filter(category__iexact = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list})
