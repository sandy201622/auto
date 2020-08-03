from app_uiauto.page.app import App
from app_uiauto.page.mobile import Mobile


class TestMobile:
    def setup_class(self):
        self.mobile = Mobile()

    # gsmCall method is only available for emulators
    def test_call(self):
        self.mobile.call("13822334455","hello")

    # sendSMS method is only available for emulators
    def test_send_mesge(self):
        self.mobile.send_mesge("13822334455","hello ddd")
