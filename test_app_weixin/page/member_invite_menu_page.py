from appium.webdriver.common.mobileby import MobileBy

from test_app_weixin.page.base_page import BasePage
from test_app_weixin.page.contact_add_page import ContactAddPage


class MemberInviteMenuPage(BasePage):

    def add_member_manual(self):
        self.find_and_click(MobileBy.XPATH, '//*[@text="手动输入添加"]')
        return ContactAddPage(self.driver)
