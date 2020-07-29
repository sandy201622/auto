import base64
import json

import requests
import yaml


class ApiRequest:

    def send(self,data:dict):
        #使用env存放各个测试环境的配置信息，接着把这个env存放到yaml文件来管理
        env=yaml.safe_load(open("./env.yaml",encoding="utf-8"))
        #把请求体中url替换成env配置文件中的url
        url=str(data["url"]).replace("test-sandy",env["test-sandy"][env["default"]])
        data["url"]=url
        # encoding=''
        if "encoding" in data.keys():
            encoding=data["encoding"]
            del data["encoding"]

        print(data)
        # data["headers"]["Host"]="test-sandy"
        #二次封装request
        # res=requests.request(method=data["method"],url=url,headers=data["headers"])
        res=requests.request(**data)
        if encoding=="base64":
            return json.loads(base64.b64decode(res.content))
        elif encoding=="provide":
            # url是让加密提供方提供远程服务解析
            return requests.post("url",data=res.content)
        else:
            return res.json()