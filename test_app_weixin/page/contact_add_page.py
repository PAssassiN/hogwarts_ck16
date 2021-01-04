from appium.webdriver.common.mobileby import MobileBy

from test_app_weixin.page.base_page import BasePage


class ContactAddPage(BasePage):

    def add_contact(self):
        self.find_and_send_keys(MobileBy.XPATH, '//*[contains(@text, "姓名")]/..//*[@text="必填"]', 'aaaaa')
        self.find_and_click(MobileBy.XPATH, '//*[contains(@text, "性别")]/..//*[@text="男"]')
        self.wait_for(MobileBy.XPATH, '//*[@text="女"]')
        self.find_and_click(MobileBy.XPATH, '//*[@text="女"]')
        self.find_and_send_keys(MobileBy.XPATH, '//*[contains(@text, "手机")]/..//*[@text="手机号"]', '13800001111')
        self.find_and_click(MobileBy.XPATH, '//*[@text="保存"]')
        return True
