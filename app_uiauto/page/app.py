import os
import logging

from appium import webdriver

from app_uiauto.page.base_page import BasePage
from app_uiauto.page.login import Login
from app_uiauto.page.main import Main


class App(BasePage):
    #自动化测试安装渠道包
    def install(self,path):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "192.168.56.105:5555"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # caps['noReset'] = "true"
        # caps['skipServerInstallation'] = True
        caps["autoGrantPermissions"] = True
        # caps['skipDeviceInitialization'] = True
        self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        if self._driver.is_app_installed("com.xueqiu.android"):
            self._driver.remove_app("com.xueqiu.android")
        # self.install_app("/Users/yelixia/Downloads/app/a.apk")
        self._driver.install_app(path)
        self._driver.launch_app()
        self._driver.implicitly_wait(5)
        return self

    def install_app(self,path):
        result_file=os.popen("adb install " + path).read()
        print(result_file)
        if "Success" in result_file:
            logging.info("install successful")
        elif "Failure" in result_file:
            logging.info("install fail")

    def uninstall_app(self,app_id):
        result=os.popen("adb uninstall " + app_id).read()
        if "Success" in result:
            logging.info("uninstall successful")
        elif "Failure" in result:
            logging.info("uninstall fail")

    def is_app_installed(self,app_id):
        result=os.popen("adb shell pm list package").read()
        if app_id in result:
            logging.info("app is existed")
            return True
        else:
            logging.info("app is not existed")
            return False


    def start(self):
        if self._driver == None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "192.168.56.101:5555"
            # caps["app"] = "192.168.56.101:5555"
            caps["appPackage"] = "io.appium.android.apis"
            caps["appActivity"] = "io.appium.android.apis.ApiDemos"
            caps['noReset'] = "true"
            caps['skipServerInstallation'] = True
            caps['uiautomationName'] = "UiAutomator2"
            caps['skipDeviceInitialization'] = True
            caps['showChromedriverLog'] = True

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.launch_app()

        self._driver.implicitly_wait(3)

        return self

    def restart(self):
        self._driver.close()
        self._driver.launch_app()

    def stop(self):
        self._driver.quit()

    def main(self) -> Main:
        return Main(self._driver)

    def login(self) -> Login:
        return Login(self._driver)
