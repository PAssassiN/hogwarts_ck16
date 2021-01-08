from test_frame.base_page import BasePage
from selenium.webdriver.common.by import By


class Search(BasePage):
    def search(self):
        self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("alibaba")
        return True
