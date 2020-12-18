from selenium import webdriver
import pytest
from time import sleep
import yaml


class TestDemo():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_id('kw').click()
        self.driver.find_element_by_id('kw').send_keys('霍格沃兹测试学院')
        self.driver.find_element_by_id('su').click()
        self.driver.find_element_by_link_text('霍格沃兹测试学院 – 测试开发工程师的黄埔军校').click()
        # sleep(3)


def test_demo():
    option = webdriver.ChromeOptions()
    # 设置debug的地址
    option.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(5)
    driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    driver.find_element_by_id('menu_contacts').click()
    print(driver.get_cookies())


# 使用cookie登陆
def test_cookie():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    # 1、先打开扫码登陆页
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?')
    cookie = [
        {'domain': '.qq.com', 'expiry': 1608226531, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
         'value': '1'},
        {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
         'value': '1688850459807483'},
        {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
         'value': '1688850459807483'},
        {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
         'value': '1970325136204626'},
        {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
         'value': 'a6954282'},
        {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
         'value': '1'},
        {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False,
         'value': '194241423'},
        {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
         'value': 'direct'},
        {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
         'value': '21878874791757435'},
        {'domain': '.qq.com', 'expiry': 1608312770, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
         'value': 'GA1.2.102647311.1608226158'},
        {'domain': 'work.weixin.qq.com', 'expiry': 1608257692, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
         'secure': False, 'value': '87r0jbr'},
        {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
         'value': 'zZmnpsxgptZDXU1YNimKuXzwAv09h3da3tT_D11J4_CZ4GXlR2n3_6D1en4cpSvrgsuR1hEs6JIgPq_uvEbX5c5R418J4g5cp70NnCynjbUP3Q-s6lPDszvEvHHGQTX0jmjZCZHJ2tm08iLOlq4p8a93aIsntpRRxjxQ5P_kvnRDr2kPsuMbIDIjyCG-JVk1bJqw4up4hzHzyg473tJRnqVNc_gYZaQWSObiBUD_6EQIFfWvNNpNmXjv3i_wsIy79FdCBVEw-fmAatTj6O-iCQ'},
        {'domain': '.work.weixin.qq.com', 'expiry': 1610818521, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
         'path': '/', 'secure': False, 'value': 'zh'},
        {'domain': '.qq.com', 'expiry': 1671298370, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
         'value': 'GA1.2.253628043.1608226158'},
        {'domain': '.work.weixin.qq.com', 'expiry': 1639762156, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/',
         'secure': False, 'value': '0'},
        {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
         'value': 'OQGV9yhwIczt85TiRvtCFCQKgC6ufaxgtOXY-6qruFR-8KHxD7IfCOxK1zXpo7ak'},
        {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False,
         'value': 'ssid=s4332547674'}]
    # 2、设置cookie
    for i in cookie:
        driver.add_cookie(i)
    # 3、打开目的页面
    driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    driver.find_element_by_id('menu_contacts').click()
    sleep(3)
    # 4、关闭页面
    driver.quit()


# 复用浏览器 + 获取保存cookie
def test_get_cookie():
    option = webdriver.ChromeOptions()
    # 设置debug的地址
    option.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(10)
    # 访问网页，拿到cookie
    driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
    cookie = driver.get_cookies()
    # 获取到的cookie写入文件
    with open('./data.yml', 'w', encoding='UTF-8') as f:
        yaml.dump(cookie, f)


# 使用上面方法获得的cookie进行登陆，此方法则不需要复用浏览器
def test_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    # 打开扫码登陆页
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?')
    # 打开获取到的cookie文件
    with open('./data.yml', encoding='UTF-8') as f:
        yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            driver.add_cookie(cookie)
    driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    sleep(2)


def test_add_member():
    option = webdriver.ChromeOptions()
    # 设置debug的地址
    option.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(10)
    driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
    # 找到添加成员的按钮
    ele = driver.find_element_by_xpath('//div[@class="ww_operationBar"]//a[@class="qui_btn ww_btn js_add_member"]')
    sleep(2)
    ele.click()
    # 输入相关信息
    driver.find_element_by_id('username').send_keys('王五')
    driver.find_element_by_id('memberAdd_acctid').send_keys('wangwu')
    driver.find_element_by_id('memberAdd_phone').send_keys('13600000000')
    # # 通过邮件或短信发送企业要求 取消勾选
    driver.find_element_by_xpath('//*[@class="member_edit_joinCheckboxCnt member_edit_sec"]//input').click()
    # # 保存
    driver.find_element_by_xpath('//div//a[text()="保存"]').click()
    # 断言
    driver.find_element_by_xpath('//*[@id="memberSearchInput"]').send_keys('王五')
    expected = driver.find_element_by_xpath(
        '//*[@id="search_member_list"]//span[@class="ww_searchResult_title_peopleName"]').text
    assert '王五' == expected
