from appium.webdriver.common.touch_action import TouchAction

from app_uiauto.page.base_page import BasePage


class Flagment(BasePage):

    def context_menu(self):
       self.find("accessibility id","Context Menu").click()
       return self

    def longPress(self):
        ele=self.find("id","io.appium.android.apis:id/long_press")
        action=TouchAction(self._driver)
        return action.long_press(ele)
