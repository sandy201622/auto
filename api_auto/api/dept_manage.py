from api_auto.api.wework import WeWork


class Dept_manage(WeWork):
    def __init__(self):
        corpsecret = "DZ1ZfzHphbUMhU4OoHDNTys8_BcRe0lG8JF3QHNqjfc"
        self.access_token = self.get_token(corpsecret)
        print(self.access_token)

    def get_dept_list(self,id=None):
        data={
            "method":"get",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/department/list",
            "params":{
                "access_token":self.access_token,
                "id":id
            }
        }
        return self.send(data)

    def create_dept(self):
        pass

    def update_dept(self):
        pass

    def delete_dept(self):
        pass