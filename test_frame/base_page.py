from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from test_frame.black_list_handle import black_wrapper


class BasePage:

    # 存放driver相关的操作
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        # 黑名单
        self.black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]

    # 直接@函数名就能调用这个函数作为装饰器使用
    @black_wrapper
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def find_and_click(self, by, locator):
        return self.driver.find_element(by, locator).click()

    # 两种滑动屏幕的方式
    def scroll_find(self, text):
        return self.driver.find_element(MobileBy.
                                        ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                             'scrollable(true).instance(0)).'
                                                             'scrollIntoView(new UiSelector().'
                                                             f'text("{text}").instance(0));')

    def swipe_find(self, by, locator):
        # 查找全部元素
        count = 0
        self.driver.implicitly_wait(1)
        elements = self.finds(by, locator)
        while len(elements) == 0 or count <= 3:
            # 一直在滑动
            self.driver.swipe(0, 600, 0, 400)
            elements = self.finds(by, locator)
            count += 1
        self.driver.implicitly_wait(5)
        return elements[0]

    def swipe_find_click(self, by, locator):
        self.swipe_find(by, locator).click()

    def scroll_find_and_click(self, text):
        self.scroll_find(text).click()

    def find_and_send_keys(self, by, locator, text):
        self.find(by, locator).send_keys(text)

    def wait_for(self, by, locator):
        # 显示等待
        def wait_ele_for(driver):
            elements = driver.find_elements(by, locator)
            return len(elements) > 0

        WebDriverWait(self.driver, 10).until(wait_ele_for)

    def get_toast_text(self):
        result = self.find(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        return result
