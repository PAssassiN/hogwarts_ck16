from selenium.webdriver.common.by import By
from test_web_weixin.page.add_member import AddMember
from test_web_weixin.page.contact_page import ContactPage
from test_web_weixin.page.base_page import BasePage


class MainPage(BasePage):
    _location_goto_member = (By.CSS_SELECTOR, '.ww_indexImg_AddMember')

    def goto_add_member(self):
        # 跳转到添加成员页面
        self.find(*self._location_goto_member).click()
        return AddMember(self.driver)

    def goto_contact(self):
        # 跳转到通讯录页面
        self.find(By.ID, 'menu_contacts').click()
        return ContactPage(self.driver)

    # 还原，回到首页
    def back_main(self):
        self.find(By.ID, 'menu_index').click()
        self.find(By.CSS_SELECTOR, "a[node-type='cancel'").click()
