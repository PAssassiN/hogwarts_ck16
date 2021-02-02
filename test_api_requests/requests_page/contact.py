import requests

from test_api_requests.requests_page.base import Base


class Contact(Base):

    def find_member(self, userid):
        params = {'userid': userid}
        find_member_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        find_member_response = self.s.get(find_member_url, params=params)
        return find_member_response.json()

    def delete_member(self, userid):
        params = {'userid': userid}
        delete_member_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        delete_member_response = self.s.get(delete_member_url, params=params)
        return delete_member_response.json()

    def add_member(self, userid, name, department, mobile):
        add_member_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = {
            "userid": userid,
            "name": name,
            "department": department,
            "mobile": mobile,
        }
        add_member_response = self.s.post(url=add_member_url, json=data)
        return add_member_response.json()

    def update_member(self, userid, name, mobile, **kwargs):
        update_member_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
        }
        data.update(kwargs)
        update_member_response = self.s.post(url=update_member_url, json=data)
        return update_member_response.json()
