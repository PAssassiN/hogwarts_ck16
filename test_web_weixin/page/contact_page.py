from selenium.webdriver.common.by import By

from test_web_weixin.page.base_page import BasePage


class ContactPage(BasePage):
    # 现有成员列表
    _location_member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    # 添加成员操作按钮
    _location_add_member_button = (
    By.XPATH, '//div[@class="ww_operationBar"]//a[@class="qui_btn ww_btn js_add_member"]')

    def add_member_button(self):
        # 为了避免触发python循环导入的机制
        from test_web_weixin.page.add_member import AddMember
        # 加个显示等待保证按钮可点击
        self.wait_click(self._location_add_member_button)
        self.find(self._location_add_member_button).click()
        return AddMember(self.driver)

    def get_member(self):
        # 获取成员列表，用于断言
        member_list = self.driver.find_elements(*self._location_member_list)
        # member_list2 = []
        # for i in member_list:
        #     member_list2.append(i.text)
        # return member_list2
        # 成员列表代码优化(列表推导式)
        member_list_res = [i.text for i in member_list]
        return member_list_res
