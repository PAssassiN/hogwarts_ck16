import requests
import json


def test_get_access_token():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwf793a42682053e6e&corpsecret=qdXH8QRbJhkgXu3jlP0S52hpFj7Y248PPawld7Tiyv4'
    token_response = requests.get(url)
    token = json.loads(token_response.text)
    return token['access_token']


def test_get_member_list():
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_get_access_token()}&userid=zhangsan'
    get_member_response = requests.get(url)
    get_member = json.loads(get_member_response.text)
    assert get_member['userid'] == 'zhangsan'


def test_add_member():
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_get_access_token()}'
    data = {
        "userid": "TomBlank",
        "name": "TomBlank",
        "department": "1",
        "mobile": "13567676666",
    }
    add_member_response = requests.post(url=url, json=data)
    add_member = json.loads(add_member_response.text)
    assert 'created' in add_member['errmsg']


def test_delete_member():
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_get_access_token()}&userid=TomBlank'
    delete_member_response = requests.get(url)
    delete_member = json.loads(delete_member_response.text)
    assert delete_member['errmsg'] == 'deleted'
