#coding:utf8
import time
import models
import json
from django.core.exceptions import  ObjectDoesNotExist

class ClientHandler(object):
    def __init__(self, client_id):
        self.client_id = client_id
        self.client_configs = {
            "project":{}
        }

    def fetch_configs(self):
        try:
            host_obj = models.Host.objects.get(id=self.client_id)
            project_list = list(host_obj.project.select_related())
            print project_list
            for project in project_list:
                print project.deploy_dir
                self.client_configs['project'][project.name] = [project.deploy_dir,project.Type]
        except ObjectDoesNotExist:
            pass
        return self.client_configs
