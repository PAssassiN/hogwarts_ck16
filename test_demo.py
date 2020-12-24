import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction


class TestDemo:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:5555",
            "platformVersion": "7.1.2",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "noReset": "true",
            "dontStopAppOnReset": "true",
            "unicodeKeyBoard": "true",
            "resetKeyBoard": "true",
            "settings[waitForIdleTimeout]": 0
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_daka(self):
        print('企业微信登陆')
        self.driver.find_element(MobileBy.XPATH, '//*[@text="工作台"]').click()
        # 滚动查找元素
        self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"次外出")]').click()
        # 显示等待
        WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)
        assert "外出打卡成功" in self.driver.page_source
