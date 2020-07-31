from api_auto.api.wework import WeWork


class Tag(WeWork):
    def __init__(self):
        corpsecret = "DZ1ZfzHphbUMhU4OoHDNTys8_BcRe0lG8JF3QHNqjfc"
        self.access_token=self.get_token(corpsecret)
        print(self.access_token)

    def get(self):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/list",
            "params": {
                "access_token": self.access_token,
            }
        }
        return self.send(data)

    def create(self,tagname, tagid):
        data={
            "method":"post",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/tag/create",
            "params": {
                "access_token": self.access_token,
            },
            "json": {
                 "tagname": tagname,
                 "tagid": tagid
            }
        }
        return self.send(data)

    def delete(self,tagid):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/delete",
            "params": {
                "access_token": self.access_token,
                "tagid": tagid
            }
        }
        return self.send(data)

    def update(self, tagname, tagid):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/update",
            "params": {
                "access_token": self.access_token,
            },
            "json": {
                "tagname": tagname,
                "tagid": tagid
            }
        }
        return self.send(data)