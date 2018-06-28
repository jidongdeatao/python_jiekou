# -*- coding: utf-8 -*-
#根据配置获取用户token
#该脚本默认配置环境：python3.6


import urllib.request
import urllib.parse
import urllib.error
import json
import logging
import ssl

import os
import sys
# rootpath=str("工程所在目录")
# syspath=sys.path
# sys.path=[]
# sys.path.append(rootpath)#将工程根目录加入到python搜索路径中
# sys.path.extend([rootpath+i for i in os.listdir(rootpath) if i[0]!="."])#将工程目录下的一级目录添加到python搜索路径中
# sys.path.extend(syspath)

def getToken(username,tenantname,password,project,IAM):
    print('Get Token ...')
    if username == '' or username =='\n':
        username =tenantname
    ssl._create_default_https_context = ssl._create_unverified_context
    url='https://'+IAM+r'/v3/auth/tokens'
    data={
        "auth": {
                "identity": {
                        "methods": ["password"],
                        "password": {
                                "user": {
                                        "name": username,
                                        "domain": {
                                                "name": tenantname
                                        },
                                        "password": password
                                }
                        }
                },
                "scope": {
                        "project": {
                                "name":project

                        }
                }
        }
    }
    data = json.dumps(data)
    data = bytes(data, 'utf8')
    #data=urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url=url,data=data)
    request.add_header('Content-Type', r'application/json')
    request.method='POST'
    resp=''
    header=''
    try:
        response=urllib.request.urlopen(request)
        resp=response.read().decode()
        header=response.headers['X-Subject-Token']
        logging.info('Get Token Success: '+header)
    except urllib.error.HTTPError as e:
        errinfo=e.read().decode()
        errinfo="Get Token Error :" + errinfo
        print(errinfo)
        logging.error(errinfo)
    except urllib.error.URLError as e:
        errinfo='Get Token Request Url Error:'+e.reason
        print(errinfo)
        logging.error(errinfo)
    else:
        print('Done Without GET Token Exception')

    return header

if __name__=='__main__':
    tenantname = 'XXXXX'
    project = 'southchina'
    IAM = '192.144.35.205:31943'
####################################
####################################
    #dms_admin Token
    username1= 'XXX_test3'
    password1= 'XXX@1'
    m1 = getToken(username1, tenantname, password1, project, IAM)
    print("\n")
    print("dms_admin Token XXX_test3:")
    print(m1)
    print("\n")

####################################
    #te_admin Token
    username2= 'XXX_test4'
    password2= 'XXX@1'
    m2 = getToken(username2, tenantname, password2, project, IAM)
    print("\n")
    print("te_admin Token XXX_test4:")
    print(m2)
    print("\n")

####################################
    #readonly Token
    username3= 'XXX_test2'
    password3= 'XXX@1'
    m3 = getToken(username3, tenantname, password3, project, IAM)
    print("\n")
    print("redonly Token XXX_test2:")
    print(m3)
    print("\n")

####################################
    #no权限 Token
    username4= 'XXX_test5'
    password4= 'XXX@1'
    m4 = getToken(username4, tenantname, password4, project, IAM)
    print("\n")
    print("no_admin Token XXX_test5:")
    print(m4)
    print("\n")
