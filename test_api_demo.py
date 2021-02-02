import requests
import json


def test_get_access_token():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwf793a42682053e6e&corpsecret=qdXH8QRbJhkgXu3jlP0S531suzE6cZ8LTwOQkJ4d1F8'
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


def test_update_member():
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_get_access_token()}'
    data = {
        "userid": 'zhangsan',
        "name": '张三',
        "mobile": '13800088000',
    }
    update_member_response = requests.post(url=url, json=data)
    update_member = json.loads(update_member_response.text)
    assert update_member['errmsg'] == 'updated'
