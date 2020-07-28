import yaml
from selenium.webdriver.common.by import By

from app_uiauto.page.Views import Views
from app_uiauto.page.accessibility import Accessibility
from app_uiauto.page.appbehavier import Appbehavier
from app_uiauto.page.base_page import BasePage


class Main(BasePage):

    def goto_accessibility(self):
        self.find('xpath','//*[@content-desc="Accessibility"]').click()
        self.set_implicitly(1)
        return Accessibility(self._driver)

    def goto_app(self):
        self.find('accessibility id','App').click()
        return Appbehavier(self._driver)

    def goto_view(self):
        self.find('accessibility id','Views').click()
        return Views(self._driver)
