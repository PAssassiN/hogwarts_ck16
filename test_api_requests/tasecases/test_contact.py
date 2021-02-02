import pytest
from test_api_requests.requests_page.contact import Contact


class TestContact:
    def setup_class(self):
        self.contact = Contact()
        self.userid = 'hello2021'
        self.name = 'hello_0202'

    @pytest.mark.parametrize("corpid, corpsecret, expected", [(None, None, 0),
                                                              ('XXX', None, 40013),
                                                              (None, 'YYY', 40001)])
    def test_get_token(self, corpid, corpsecret, expected):
        r = self.contact.get_token(corpid, corpsecret)
        assert r.get('errcode') == expected

    def test_add_member(self):
        self.contact.add_member(userid=self.userid, name=self.name, department=1, mobile='13820210202')
        try:
            # add_member创建成员后，去查询一下是否存在
            find_after_add = self.contact.find_member(self.userid)
        finally:
            # 数据清洗
            self.contact.delete_member(self.userid)
        assert find_after_add['name'] == self.name

    def test_find(self):
        r = self.contact.find_member("wangwu")
        assert r.get('name') == '王五'

    def test_delete_member(self):
        self.contact.add_member(userid='lao6', name='老刘6', department=1, mobile='19880210202')
        r = self.contact.delete_member('lao6')
        assert r.get('errmsg') == "deleted"
