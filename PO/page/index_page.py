from PO.page.login_page import LoginPage
from PO.page.register_page import RegisterPage


class IndexPage:

    def goto_login(self):
        # 跳转到登陆页面
        return LoginPage()

    def goto_register(self):
        # 跳转到注册页面
        return RegisterPage()
