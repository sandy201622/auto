from appium.webdriver.common.touch_action import TouchAction

from app_uiauto.page.base_page import BasePage


class Activity(BasePage):
    #移动手势
    def hello_world(self):
        start_ele = self.find('xpath', '//*[@text="Animation"]')
        end_ele = self.find('accessibility id', 'Hello World')
        self.move_mouse(start_ele,end_ele)
        return self

    # 滚动屏幕
    def recreate(self):
       self.scroll_screen('description',"Recreate").click()
       return self.find('xpath','//*[@class="android.widget.Button"]').text