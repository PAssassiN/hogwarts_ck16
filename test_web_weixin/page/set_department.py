from test_web_weixin.page.base_page import BasePage
from selenium.webdriver.common.by import By


class SetDepartment(BasePage):
    # 部门名称
    _location_department_name = (By.CSS_SELECTOR, '[name=name]')
    # 所属部门
    _location_the_department1 = (By.CSS_SELECTOR, ".js_toggle_party_list span.js_parent_party_name")
    # 展开后的部门
    _location_the_department2 = (By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id='1688850459807484_anchor']")
    # 保存按钮
    _location_save_button = (By.CSS_SELECTOR, '.ww_btn_Blue[d_ck="submit"]')

    def set_department(self):
        from test_web_weixin.page.contact_page import ContactPage
        self.wait_click(self._location_department_name)
        self.find(*self._location_department_name).send_keys('财务部')
        # 所属部门
        self.wait_click(self._location_the_department1)
        self.find(*self._location_the_department1).click()
        self.wait_click(self._location_the_department2)
        self.find(*self._location_the_department2).click()
        # 保存按钮
        self.find(*self._location_save_button).click()
        return ContactPage(self.driver)
