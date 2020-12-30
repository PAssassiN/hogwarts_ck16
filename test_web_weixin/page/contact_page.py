from selenium.webdriver.common.by import By
from test_web_weixin.page.base_page import BasePage
from test_web_weixin.page.set_department import SetDepartment
from time import sleep


class ContactPage(BasePage):
    # 现有成员列表
    _location_member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    # 添加成员操作按钮
    _location_add_member_button = (
    By.XPATH, '//div[@class="ww_operationBar"]//a[@class="qui_btn ww_btn js_add_member"]')
    # 添加按钮
    _location_add_button = (By.XPATH, '//*[@class="member_colLeft_top_addBtn"]')
    # 添加部门按钮
    _location_set_department_button = (By.CSS_SELECTOR, '.js_create_party')
    # 部门列表
    _location_memberList = (By.CSS_SELECTOR, '.jstree-children a:nth-child(3)')

    def add_member_button(self):
        # 为了避免触发python循环导入的机制
        from test_web_weixin.page.add_member import AddMember
        # 加个显示等待保证(添加成员)按钮可点击
        self.wait_click(self._location_add_member_button)
        self.find(self._location_add_member_button).click()
        return AddMember(self.driver)

    def get_member(self):
        # 获取成员列表，用于断言
        self.wait_click(self._location_member_list)
        member_list = self.finds(*self._location_member_list)
        # member_list2 = []
        # for i in member_list:
        #     member_list2.append(i.text)
        # return member_list2
        # 成员列表代码优化(列表推导式)
        member_list_res = [i.text for i in member_list]
        return member_list_res

    def set_department_button(self):
        # from test_web_weixin.page.contact_page import ContactPage
        # 1、点击添加子部门按钮 3、跳转到设置子部门页
        self.wait_click(self._location_add_button)
        self.find(*self._location_add_button).click()
        self.wait_click(self._location_set_department_button)
        self.find(*self._location_set_department_button).click()
        return SetDepartment(self.driver)

    def get_department_list(self):
        self.driver.refresh()
        sleep(2)
        # 获取成员列表，用于断言
        self.wait_click(self._location_memberList)
        member_list = self.finds(*self._location_memberList)
        # 成员列表代码优化(列表推导式)
        member_list_res = [i.text for i in member_list]
        print(member_list_res)
        return member_list_res
