import random

import pytest

from api_auto.api.address import Address


class TestAddress:
    def setup_class(self):
        self.address=Address()

    def test_get(self):
        resJson=self.address.get("sandy9")
        print(resJson)
        assert resJson['errmsg'] == "ok"

    # 准备测试数据userid、name、mobile
    create_data = [('sandy' + str(x), "sandy", '138%08d' % x) for x in range(10)]
    @pytest.fixture(scope="module")
    def userinfo(self,request):
        data=request.param
        return data

    # @pytest.mark.parametrize("userid, name, mobile", [("xxx","dddd","13811223322")])
    @pytest.mark.parametrize("userinfo", create_data, indirect=True)
    def test_create(self,userinfo):
        resJson=self.address.create(*userinfo)
        assert resJson['errmsg'] == 'created'

    @pytest.mark.parametrize("userid, name, mobile", [("xxx","ewwewr","13322221111")])
    def test_update(self,userid, name, mobile):
        resJson=self.address.update(userid, name, mobile)
        assert resJson['errmsg']== 'updated'

    @pytest.mark.parametrize("userid", ["ewwewr","xxx"])
    def test_delete(self,userid):
        resJson=self.address.get(userid)
        if "userid not found" in resJson['errmsg']:
            resJsondel=self.address.delete(userid)
            assert resJsondel['errcode'] == 60111
            self.address.create(userid,
                                "test" + str(random.randint(0, 100)), "136" + str(random.randint(11110000, 11119999)))
            assert self.address.get(userid)['errcode'] == 0
            resJsondel = self.address.delete(userid)
            assert resJsondel['errmsg'] == "deleted"
        else:
            resJsondel=self.address.delete(userid)
            assert resJsondel['errmsg'] == "deleted"
