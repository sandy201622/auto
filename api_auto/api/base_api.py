import base64
import json
import os
import sys

import allure
import requests
import yaml


projectpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
print("项目路径",projectpath)

class BaseAPI:

    def send(self, data: dict):
        # 使用env存放各个测试环境的配置信息，接着把这个env存放到yaml文件来管理
        env = yaml.safe_load(open(projectpath+"/resource/env.yaml", encoding="utf-8"))
        # 把请求体中url替换成env配置文件中的url
        data["url"] = str(data["url"]).replace("test-sandy", env["test-sandy"][env["default"]])
        self.encoding=''
        if "encoding" in data.keys():
            self.encoding = data["encoding"]
            del data["encoding"]
        allure.attach(str(data), attachment_type=allure.attachment_type.TEXT)
        # 二次封装request
        res = requests.request(**data)
        if self.encoding == "base64":
            return json.loads(base64.b64decode(res.content))
        elif self.encoding == "provide":
            # url是让加密提供方提供远程服务解析
            return requests.post("url", data=res.content)
        else:
            return res.json()
