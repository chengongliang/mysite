#coding:utf8
import time
import models
import json
from django.core.exceptions import  ObjectDoesNotExist

class ClientHandler(object):
    def __init__(self, client_id):
        self.client_id = client_id
        #初始化项目字典
        self.client_configs = {
            "project":{}
        }

    def fetch_configs(self):
        try:
            #获取hostname
            host_obj = models.Host.objects.get(id=self.client_id)
            print host_obj
            #获取项目列表
            project_list = list(host_obj.project.select_related())
            print project_list
            #获取项目部署目录
            for project in project_list:
                print project.deploy_dir
                self.client_configs['project'][project.name] = [project.deploy_dir,project.Type]
        except ObjectDoesNotExist:
            pass
        return self.client_configs
