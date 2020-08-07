from app_uiauto.page.app import App


class TestFlagment:

    def setup(self):
        self.flagment=App().start().main().goto_app().goto_flagment()

    def test_context_menu(self):
        self.context_menu_list=self.flagment.context_menu().context_menu().find_and_get_text("xpath",'//*[@text="Menu B"]')
        assert "Menu B" == self.context_menu_list



