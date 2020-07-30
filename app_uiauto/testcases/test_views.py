from app_uiauto.page import Views
from app_uiauto.page.app import App


class TestViews:
    def setup(self):
        self.app=App()
        self.views=self.app.start().main().goto_view()

    def test_popmenu(self):
        self.toast_text=self.views.popmenu()
        # 获取toastText来断言是否正确
        assert self.toast_text=="Clicked popup menu item Search"


