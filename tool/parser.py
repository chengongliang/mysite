#coding:utf8

import json
import urllib
import urllib2
from conf import settings

class Parser_conf(object):
    def __init__(self):
        self.deploy_info = {}

    def load_configs(self):
        request_type = settings.configs['urls']['get_configs'][1]
        url = "%s/%s" %(settings.configs['urls']['get_configs'][0], settings.configs['HostID'])
        latest_configs = self.url_request(request_type,url)
        latest_configs = json.loads(latest_configs)
        self.deploy_info.update(latest_configs)    

    def url_request(self,action,url,**extra_data):
        abs_url = "http://%s:%s/%s" % (settings.configs['Server'],
                                       settings.configs["ServerPort"],
                                       url)
        if action in ('get','GET'):
            print abs_url,extra_data
            try:
                req = urllib2.Request(abs_url)
                req_data = urllib2.urlopen(req,timeout=settings.configs['RequestTimeout'])
                callback = req_data.read()
                print "-->server response:",callback
                return callback
            except urllib2.URLError,e:
                exit("\033[31;1m%s\033[0m"%e)

if __name__ == "__main__":
    p = Parser_conf()
    p.load_configs()
