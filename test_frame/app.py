from appium import webdriver
from test_frame.base_page import BasePage
from test_frame.page.main import Main


class App(BasePage):
    # app启动时的通用参数
    def start(self):
        if self.driver == None:
            desired_caps = {
                "platformName": "Android",
                "deviceName": "127.0.0.1:5555",
                "platformVersion": "7.1.2",
                "appPackage": "com.xueqiu.android",
                "appActivity": ".view.WelcomeActivityAlias",
                "noReset": "true",
                "dontStopAppOnReset": "true",
                "unicodeKeyBoard": "true",
                "resetKeyBoard": "true",
                "automationName": "UiAutomator2",
                "settings[waitForIdleTimeout]": 0
            }
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()

        return self

    def goto_main(self):
        return Main(self.driver)
