# coding=utf-8
import tornado
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
import constants
import json
import time


class AccessToken(object):

    _access_token = None
    _create_time = 0
    _expires_in = 0

    @classmethod
    @tornado.gen.coroutine
    def update_access_token(cls):
        client = AsyncHTTPClient()
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' %(constants.WECHAT_APPID, constants.WECHAT_APPSECRET)
        resp = yield client.fetch(url)
        dict_data = json.loads(resp.body.decode('utf-8'))
        print(dict_data)
        if 'errcode' in dict_data:
            raise Exception('wechat server error')
        else:
            cls._access_token = dict_data["access_token"]
            cls._expires_in = dict_data["expires_in"]
            cls._create_time = time.time()


    @classmethod
    @tornado.gen.coroutine
    def get_access_token(cls):
        if time.time() - cls._create_time > (cls._expires_in - 200):
            yield cls.update_access_token()
            raise tornado.gen.Return(cls._access_token)
        else:
            raise tornado.gen.Return(cls._access_token)
