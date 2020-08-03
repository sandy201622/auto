from appium import webdriver

from app_uiauto.page.app import App
from app_uiauto.page.base_page import BasePage


class Mobile(BasePage):
    # todo 如何把driver传递进来，不用这样init，需改善
    def __init__(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "192.168.56.101:5555"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = "io.appium.android.apis.ApiDemos"
        # 不清除app缓存
        caps['noReset'] = "true"
        # 不每次安装server
        caps['skipServerInstallation'] = True
        caps['uiautomationName'] = "UiAutomator2"
        caps['skipDeviceInitialization'] = True
        # 需要输入中文
        # caps['unicodeKeyBoard'] = True
        # caps['resetKeyBoard'] = True

        # caps['showChromedriverLog'] = True
        caps['chromedriverExecutable'] = "/Users/yelixia/PycharmProjects/AppiumDemo10/chromedriver/2.29/chromedriver"

        self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)


    def call(self,num,mesge):
        self._driver.make_gsm_call(num,mesge)

    def send_mesge(self,num,mesge):
        self._driver.send_sms(num,mesge)

    def switch_network(self,con_type):
        self._driver.get_screenshot_as_png("./photos/img.png")
        self._driver.set_network_connection(con_type)
        self._driver.get_screenshot_as_png("./photos/img.png")