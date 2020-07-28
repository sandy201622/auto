from app_uiauto.page.base_page import BasePage


class Login(BasePage):
    def get_mobile_login(self):
       return self.find_and_get_text('id','com.xueqiu.android:id/tv_login_by_phone_or_others')