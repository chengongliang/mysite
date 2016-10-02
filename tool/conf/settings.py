#_*_coding:utf-8_*_

configs ={
    'HostID': 1,
    "Server": "localhost",
    "ServerPort": 8000,
    "urls":{

        'get_configs' :['api/client/config','get'],
        'deploy_data_report': ['api/client/deploy_info/report/','post'],

    },
    'RequestTimeout':30,
    'Temp_dir': "/tmp/deploy_tmp/",
}
