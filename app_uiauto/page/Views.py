from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from app_uiauto.page.base_page import BasePage


class Views(BasePage):
    def popmenu(self):
        self.scroll_screen("description","Popup Menu").click()
        self.find("xpath",'//*[@content-desc="Make a Popup!"]').click()
        self.find("xpath",'//*[@text="Search"]').click()
        # 通过底层机制uiautomator2抓取toast，然后添加到dom里，但是本身不属于控件，所有必须使用xpath来定位，通过class，或者text
        return self.find("xpath",'//*[@class="android.widget.Toast"]').text

    #测试混合app的webveiw
    def into_webview(self):
        '''
        1. canpability添加这个配置：
        当需要1种chromedriver时----》“chromedriverExecute”=“指定driver地址”
        当需要多个chromedriver时，使用下面的方式：
        “chromedriverExecutableDir”=“指定chromedriver目录”
        “chromedriverChromeMappingFile” = ”../mapping.json"

        2. 通过切换上下文 switch_to.context, 进入webview页面，之后可以使用selenium方式来操控元素
        不建议by accessibility id来定位，因为不同设备渲染页面也不同，兼容性也不同，所以通过切换上下文

        3. 当在webview页面上点击后进入新窗口时，需要切换switch_to.window 

        4. 当页面加载css比较慢时，需要添加显性等待机制
        :return:
        '''
        print(self._driver.contexts)
        self.scroll_screen("description", "WebView").click()
        print(self._driver.contexts)
        # WebDriverWait(self._driver, 10, 1).until(lambda x: "WEBVIEW_com.xueqiu.android" in self._driver.contexts)
        self._driver.switch_to.context(self._driver.contexts[-1])
        WebDriverWait(self._driver, 10).until(
            expected_conditions.visibility_of_element_located((MobileBy.ID, "i_am_a_textbox")))
        print(self._driver.page_source)
        self._driver.find_element(MobileBy.ID,"i_am_a_textbox").send_keys("i am sandy")
        self.find("id","i am a link").click()
        print(self._driver.page_source)