import os

import pytest
import yaml

from app_uiauto.page.app import App

projectpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# print("1111111",os.path.dirname(__file__))
# print("222222",os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

class TestMenu:
    def setup(self):
        self.menu=App().start().main().goto_app().goto_menu()

    @pytest.mark.parametrize('menu_name,expected',yaml.safe_load(open(projectpath + '/datas/menu.yaml',encoding='utf-8')))
    def test_click_menu(self,menu_name,expected):
        assert self.menu.click_menu(menu_name)==expected