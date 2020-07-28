from app_uiauto.page.app import App


class TestActivity:
    def setup_class(self):
        self.app=App()
        self.activity=self.app.start().main().goto_app().goto_activity()

    def test_move(self):
        self.activity.hello_world()

    def test_scroll(self):
        assert self.activity.recreate()=='RECREATE'

    def deardown(self):
        self.app.back()

    def deardown_class(self):
        self.app.stop()

