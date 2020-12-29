from PO.page.index_page import IndexPage


class TestIndex:

    def setup_class(self):
        # 实例变量可以在类的其他方法使用
        self.index_page = IndexPage()

    def test_login(self):
        # 1、跳转到登陆页，2、在登陆页扫码登陆
        self.index_page.goto_login()

    def test_register(self):
        # 1、跳转到注册页，2、在注册页进行注册
        self.index_page.goto_register()
