import os

import allure
import pytest
import yaml

from app_uiauto.page.app import App


class TestInstallApp:
    # def setup(self):
    #     path="/Users/yelixia/Downloads/app/a.apk"
    #     self.login_mode=App().install(path).login()
    @pytest.mark.parametrize('packagename',yaml.safe_load(open('../datas/install_package.yaml', encoding='utf-8')))
    def test_install(self,packagename):
        path = os.path.join(os.path.split(os.path.dirname(__file__))[0],'datas/app')
        print("目录"+path)
        allure.description("安装"+path)
        self.login_mode = App().install(path+'/'+packagename).login()
        assert self.login_mode.get_mobile_login()=='手机及其他登录'




