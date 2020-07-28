import pytest
import yaml

from app_uiauto.page.app import App


class TestMenu:
    def setup(self):
        self.menu=App().start().main().goto_app().goto_menu()

    @pytest.mark.parametrize('menu_name,expected',yaml.safe_load(open('../datas/menu.yaml',encoding='utf-8')))
    def test_click_menu(self,menu_name,expected):
        assert self.menu.click_menu(menu_name)==expected