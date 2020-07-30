from app_uiauto.page.base_page import BasePage


class Views(BasePage):
    def popmenu(self):
        self.scroll_screen("description","Popup Menu").click()
        self.find("xpath",'//*[@content-desc="Make a Popup!"]').click()
        self.find("xpath",'//*[@text="Search"]').click()
        # 通过底层机制uiautomator2抓取toast，然后添加到dom里，但是本身不属于控件，所有必须使用xpath来定位，通过class，或者text
        return self.find("xpath",'//*[@class="android.widget.Toast"]').text

    def into_webview1(self):
        pass