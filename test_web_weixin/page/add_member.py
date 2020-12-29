from selenium.webdriver.common.by import By
from test_web_weixin.page.contact_page import ContactPage
from test_web_weixin.page.base_page import BasePage


class AddMember(BasePage):
    # 添加成员操作(_号为了避免暴露元素给外部)
    _location_username = (By.ID, 'username')
    _location_acctid = (By.ID, 'memberAdd_acctid')
    _location_Add_phone = (By.ID, 'memberAdd_phone')
    _location_cancel = (By.XPATH, '//*[@class="member_edit_joinCheckboxCnt member_edit_sec"]//input')
    _location_save = (By.XPATH, '//div//a[text()="保存"]')
    _location_acctid_error_message = (
    By.CSS_SELECTOR, ".member_edit_item_right.ww_inputWithTips_WithErr .ww_inputWithTips_tips")
    _location_phone_error_message = (
    By.CSS_SELECTOR, ".member_edit_item_right.ww_inputWithTips_WithErr .ww_inputWithTips_tips")
    _location_error = (By.CSS_SELECTOR, ".ww_inputWithTips_tips")

    def add_member(self):
        # 输入相关信息，*号是解元组
        self.driver.find_element(*self._location_username).send_keys('王五')
        self.driver.find_element(*self._location_acctid).send_keys('wangwu')
        self.driver.find_element(*self._location_Add_phone).send_keys('13600000000')
        # # 通过邮件或短信发送企业要求 取消勾选
        self.driver.find_element(*self._location_cancel).click()
        # # 保存
        self.driver.find_element(*self._location_save).click()
        return ContactPage(self.driver)

    def add_member_fail(self, acctid, phone):
        # 添加成员失败操作
        self.driver.find_element(*self._location_username).send_keys('王五')
        self.driver.find_element(*self._location_acctid).send_keys(acctid)
        self.driver.find_element(*self._location_Add_phone).send_keys(phone)
        self.driver.find_element(*self._location_save).click()
        # 加个显示等待
        acctid_error_message = self.wait_click(self._location_acctid_error_message).text
        phone_error_message = self.wait_click(self._location_phone_error_message).text
        error_list = [acctid_error_message, phone_error_message]
        # 方法2
        # res = self.finds(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        # print(res)
        # error_list = [i.text for i in res]
        # print(error_list)
        return error_list
