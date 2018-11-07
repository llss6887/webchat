import json

import tornado
from tornado.httpclient import AsyncHTTPClient
from tornado.httpserver import HTTPRequest

from utils import AccessToken
from handles import BaseHandles


class AddMenu(BaseHandles.BaseHandle):
    @tornado.gen.coroutine
    def get(self):
        try:
            token = yield AccessToken.get_access_token()
        except Exception as e:
            self.write("errmsg: %s" % e)
        else:
            client = AsyncHTTPClient()
            url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % token
            menu = {
                "button": [
                    {
                        "name": "缴费",
                        "type": "view",
                        "url": "http://heimamba.com/wechat/profiles"
                    },
                    {
                        "type": "view",
                        "name": "报修",
                        "url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx4ccc7659371cb250&redirect_uri=http://heimamba.com/wechat/baoxiu&response_type=code&scope=snsapi_userinfo&state=1&connect_redirect=1#wechat_redirect"
                    },
                    {
                        "type": "view",
                        "name": "我的",
                        "key": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx4ccc7659371cb250&redirect_uri=http://heimamba.com/wechat/profile&response_type=code&scope=snsapi_userinfo&state=1&connect_redirect=1#wechat_redirect"
                    }
                ]
            }
            req = HTTPRequest(url=url, method='POST', body=json.dumps(menu, ensure_ascii=False))
            resp = yield client.fetch(req)
            dict_data = json.loads(resp.body.decode('utf-8'))
            print(dict_data)
            if dict_data['errcode'] == 0:
                self.write('OK')
            else:
                self.write('error')


class DeleteMenu(BaseHandles.BaseHandle):
    @tornado.gen.coroutine
    def get(self):
        try:
            token = yield AccessToken.get_access_token()

        except Exception as e:
            self.write("errmsg: %s" % e)
        else:
            client = AsyncHTTPClient()
            resp = yield client.fetch('https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s' % token)
            dict_data = json.loads(resp.body.decode('utf-8'))
            if dict_data['errcode'] == 0:
                self.write('OK')
            else:
                self.write('error')