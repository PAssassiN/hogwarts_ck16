from test_web_weixin.page.main_page import MainPage
import pytest


class TestAddMember:
    def setup_class(self):
        self.main = MainPage()

    def test_add_member(self):
        # 添加成员测试用例
        # 1、跳转到添加成员页 2、添加成员 3、自动跳转到通讯录 4、获取成员列表进行断言
        res = self.main.goto_add_member().add_member().get_member()
        assert '王五' in res

    @pytest.mark.parametrize("acctid, phone, expect_res",
                             [('lisi', '13999000000', '该帐号已被“李四”占有'),
                              ('abc', '13800000000', '该手机号已被“张三”占有')])
    # 第一次参数化， 传入重复的accid， 正确的手机号， 断言信息
    # 第一次参数化， 传入正确的accid， 重复的手机号， 断言信息
    def test_add_member_fail(self, acctid, phone, expect_res):
        # 添加成员失败测试用例
        res = self.main.goto_add_member().add_member_fail(acctid, phone)
        assert expect_res in res

    def test_add_member_by_contact(self):
        # 通过通讯录添加成员
        res = self.main.goto_contact().add_member_button().add_member().get_member()
        assert '王五' in res

    def teardown(self):
        # 此处有BUG，部分用例没有back_main()下的第二个driver元素
        self.main.back_main()
        pass

    def teardown_class(self):
        self.main.quit()
        pass
