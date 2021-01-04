from appium.webdriver.common.mobileby import MobileBy

from test_app_weixin.page.base_page import BasePage
from test_app_weixin.page.member_invite_menu_page import MemberInviteMenuPage


class AddressListPage(BasePage):

    def click_add_member(self):
        # 添加成员
        # self.scroll_find_and_click('添加成员')
        self.swipe_find_click(MobileBy.XPATH, '//*[@text="添加成员"]')
        return MemberInviteMenuPage(self.driver)
