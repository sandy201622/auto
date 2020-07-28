from app_uiauto.page.base_page import BasePage


class Accessibility(BasePage):
    def get_accessbility_node_provider(self):
        print(self._driver.page_source)
        self.find('accessibility id','Accessibility Node Provider').click()
        return self.find_and_get_text('xpath','//*[@text="Accessibility/Accessibility Node Provider"]')

    def check_node_querying_takeOutTrash(self):
        self.find("accessibility id","Accessibility Node Querying").click()
        checked=self.find("xpath",'//*[@text="Take out Trash"]/following-sibling::*[1]').get_attribute('checked')
        if checked=='true':
            return True
        else:
            self.find("xpath",'//*[@text="Take out Trash"]/following-sibling::*[1]').click()
            return self.find("xpath",'//*[@text="Take out Trash"]/following-sibling::*[1]').get_attribute('checked')

    def check_node_querying_conquerWorld(self):
        self.set_implicitly(2)
        self.find("accessibility id", "Accessibility Node Querying").click()
        checked = self.find("xpath", '//*[@text="Conquer World"]/following-sibling::*[1]').get_attribute('checked')
        if checked=='true':
            return True
        else:
            self.find("xpath", '//*[@text="Conquer World"]/following-sibling::*[1]').click()
            checked=self.find("xpath", '//*[@text="Conquer World"]/following-sibling::*[1]').get_attribute('checked')
            return True


