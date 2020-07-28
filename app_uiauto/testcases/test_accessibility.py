from app_uiauto.page.app import App


class TestAccessibility:
    def setup(self):
        self.accessibility=App().start().main().goto_accessibility()

    def test_Node_provider(self):
        assert self.accessibility.get_accessbility_node_provider()=="Accessibility/Accessibility Node Provider"

    def test_check_node_querying_takeOutTrash(self):
        assert self.accessibility.check_node_querying_takeOutTrash()

    def test_check_node_querying_conquerWorld(self):
        checked=self.accessibility.check_node_querying_conquerWorld()
        assert checked
