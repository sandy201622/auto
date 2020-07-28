from app_uiauto.page.app import App


class TestDialogs:
    def setup(self):
        self.app=App()
        self.dialogs=self.app.start().main().goto_app().goto_dialogs()

    def test_dialogs_message(self):
        self.dialogs.dialogs_messge()
