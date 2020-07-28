import inspect
import json
import yaml
from appium.webdriver import WebElement
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver

from app_uiauto.page.wrapper import handle_black


class BasePage:
    #存放测试步骤驱动里的参数
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def set_implicitly(self, time):
        self._driver.implicitly_wait(time)

    def screenshot(self, name):
        self._driver.save_screenshot(name)

    def move_mouse(self,start_ele,end_ele):
        action = TouchAction(self._driver)
        action.press(start_ele).wait(100).move_to(end_ele).wait(100).release().perform()

    def scroll_screen(self,locator,value):
        return self.find('-android uiautomator','new UiScrollable(new UiSelector().scrollable(true).instance(0))\
               .scrollIntoView(new UiSelector().'+ locator + '("'+ value + '").instance(0))')

    def finds(self, locator, value: str = None):
        elements: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    @handle_black
    def find(self, locator, value: str = None):
        element: WebElement
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element

    @handle_black
    def find_and_get_text(self, locator, value: str = None):
        element: WebElement
        if isinstance(locator, tuple):
            element_text = self._driver.find_element(*locator).text
        else:
            element_text = self._driver.find_element(locator, value).text
        return element_text

    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            # 获取哪个测试用例的步骤
            name = inspect.stack()[1].function
            steps = yaml.safe_load(f)[name]
        raw = json.dumps(steps)
        for key, value in self._params.items():
            raw = raw.replace('${' + key + '}', value)
        steps = json.loads(raw)
        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                if "click" == action:
                    self.find(step["by"], step["locator"]).click()
                if "send" == action:
                    self.find(step["by"], step["locator"]).send_keys(step["value"])
                if "len > 0" == action:
                    eles = self.finds(step["by"], step["locator"])
                    return len(eles) > 0

    def back(self):
        self._driver.back()
