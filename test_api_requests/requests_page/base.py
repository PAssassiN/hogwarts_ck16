import requests
from requests import Session


class Base:
    def __init__(self):
        self.s = Session()
        self.corpid = 'wwf793a42682053e6e'
        self.corpsecret = 'qdXH8QRbJhkgXu3jlP0S531suzE6cZ8LTwOQkJ4d1F8'
        self.s.params["access_token"] = self.get_token().get("access_token")

    def get_token(self, corpid=None, corpsecret=None):
        if corpid is None:
            corpid = self.corpid
        if corpsecret is None:
            corpsecret = self.corpsecret
        params = {"corpid": corpid, "corpsecret": corpsecret}
        token_response = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=params)
        return token_response.json()
