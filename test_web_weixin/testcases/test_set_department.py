from test_web_weixin.page.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        self.main = MainPage()

    def test_set_department(self):
        res = self.main.goto_contact().set_department_button().set_department().get_department_list()
        assert '财务部' in res
