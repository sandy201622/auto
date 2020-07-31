import pytest

from api_auto.api.base_api import BaseAPI
from api_auto.api.wework import WeWork


class Address(WeWork):
    def __init__(self):
        corpsecret = "DZ1ZfzHphbUMhU4OoHDNTys8_BcRe0lG8JF3QHNqjfc"
        self.access_token=self.get_token(corpsecret)
        print(self.access_token)

    def get(self,userid):
        data={
            "method":"get",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params": {
                "access_token": self.access_token,
                "userid": userid
            }
        }
        return self.send(data)

    def create(self,userid, name, mobile):
        data={
            "method":"post",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params":{
                "access_token":self.access_token
            },
            "json":{
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": [1]
            }
        }
        return self.send(data)

    def update(self,userid ,name, mobile):
        data={
            "method":"post",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "params": {
                "access_token": self.access_token
            },
            "json":{
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": [1]
            }
        }
        print(self.access_token)
        return self.send(data)

    def delete(self,userid):
        data={
            "method":"get",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params": {
                "access_token": self.access_token,
                "userid":userid
            }
        }
        return self.send(data)

