from app_uiauto.page.base_page import BasePage


class Dialogs(BasePage):
    def dialogs_messge(self):
        self.find('id','io.appium.android.apis:id/two_buttons').click()
        # self._driver.switch_to_alert()
        self.find('id','android:id/button2').click()
        return self