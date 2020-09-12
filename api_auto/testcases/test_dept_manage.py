import json

import pytest

from api_auto.api.dept_manage import Dept_manage


class Test_dept_manage:
    def setup(self):
        self.dept=Dept_manage()

    @pytest.mark.parametrize("id",[1,2,3,7])
    def test_get_dept_list(self,id):
        res =self.dept.get_dept_list()
        print(res)
        assert res['errmsg']=='ok'

