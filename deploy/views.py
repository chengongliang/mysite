#coding:utf8
from django.shortcuts import render,HttpResponse
from serializer import  ClientHandler
import json

# Create your views here.
# 配置解析api
def client_configs(request,client_id):
    print("--->",client_id)
    config_obj = ClientHandler(client_id)
    config = config_obj.fetch_configs()
    if config:
        return HttpResponse(json.dumps(config))

def deploy_data_report(request):
    if request.method == 'POST':
        print "---->",request.POST
