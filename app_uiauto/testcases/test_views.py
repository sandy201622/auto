import pytest

from app_uiauto.page import Views
from app_uiauto.page.app import App


class TestViews:
    def setup(self):
        self.app = App()
        self.views = self.app.start().main().goto_view()

    def test_popmenu(self):
        self.toast_text = self.views.popmenu()
        # 获取toastText来断言是否正确
        assert self.toast_text == "Clicked popup menu item Search"

    def test_webview(self):
        self.views.into_webview()


# 需要配置python解释器环境，来跑这个python运行入口程序
# if __name__ == "__main__":
#     pytest.main(['-vs','test_views.py::TestViews::test_popmenu'])
