from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from app_uiauto.page.Dialogs import Dialogs
from app_uiauto.page.activity import Activity
from app_uiauto.page.base_page import BasePage


class Appbehavier(BasePage):
    def goto_menu(self):
        self.find('accessibility id','Menu').click()
        WebDriverWait(self._driver,4).until(expected_conditions.visibility_of_element_located\
                                                ((By.XPATH,'//*[@text="Inflate from XML"]')))
        self.find('xpath','//*[contains(@text,"from XML")]').click()
        self.find('id',"io.appium.android.apis:id/spinner").click()

        return self

    def click_menu(self,menu_name):
        self.find('xpath','//*[contains(@text,"'+ menu_name +'")]').click()
        return self.find('id','android:id/text1').text

    def goto_activity(self):
        self.find('xpath','//*[@text="Activity"]').click()
        return Activity(self._driver)

    def goto_dialogs(self):
        self.find('xpath','//*[@text="Alert Dialogs"]').click()
        return Dialogs(self._driver)




