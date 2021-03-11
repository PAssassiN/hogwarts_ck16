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

'''
def test_demo():
    option = webdriver.ChromeOptions()
    # 设置debug的地址
    option.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(5)
    driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    driver.find_element_by_id('menu_contacts').click()
    department_list_xpath = '//ul[@class="jstree-children"]'
    department_list = driver.find_element_by_xpath(department_list_xpath).text
    print(department_list)
'''

'''
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
'''

'''
# 使用上面方法获得的cookie进行登陆，此方法则不需要复用浏览器
def test_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    # 打开扫码登陆页
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?')
    # 打开获取到的cookie文件
    with open('../test_web_weixin/testcases/data.yml', encoding='UTF-8') as f:
        yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            driver.add_cookie(cookie)
    driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    sleep(2)

'''

'''
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
    # 断言，通过在memberSearchInput输入此成员名字，有结果显示在searchResult上，来判断添加成功
    driver.find_element_by_xpath('//*[@id="memberSearchInput"]').send_keys('王五')
    expected = driver.find_element_by_xpath(
        '//*[@id="search_member_list"]//span[@class="ww_searchResult_title_peopleName"]').text
    assert '王五' == expected
'''

