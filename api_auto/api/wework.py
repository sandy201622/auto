import pytest

from api_auto.api.base_api import BaseAPI


class WeWork(BaseAPI):
    def get_token(self,secret):
        corpid = "wwcffbbc0200a5f2ba"
        corpsecret = secret
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": corpid,
                "corpsecret": corpsecret
            }
        }

        return self.send(data)["access_token"]