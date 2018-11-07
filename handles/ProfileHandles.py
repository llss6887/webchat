# coding=utf-8

import json
import tornado
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from handles import BaseHandles
import constants
from utils import AccessToken


class ProfileHandler(BaseHandles.BaseHandle):
    # @tornado.gen.coroutine
    # def get(self):
    #     code = self.get_argument("code")
    #     client = AsyncHTTPClient()
    #     url = "https://api.weixin.qq.com/sns/oauth2/access_token?" \
    #           "appid=%s&secret=%s&code=%s&grant_type=authorization_code" % (
    #               constants.WECHAT_APPID, constants.WECHAT_APPSECRET, code)
    #     resp = yield client.fetch(url)
    #     dict_data = json.loads(resp.body.decode('utf-8'))
    #     print(dict_data)
    #     if "errcode" in dict_data:
    #         self.write("error occur")
    #     else:
    #         access_toke = dict_data["access_token"]
    #         open_id = dict_data["openid"]
    #         url = "https://api.weixin.qq.com/sns/userinfo?" \
    #               "access_token=%s&openid=%s&lang=zh_CN" % (access_toke, open_id)
    #         resp = yield client.fetch(url)
    #         user_data = json.loads(resp.body.decode('utf-8'))
    #         sql = 'select wx_name, name, idcard, open_id, phone, xq_name, xq_louhao, xq_address, wx_head_image from t_user_info where open_id=%(openod)s'
    #         sql_user = self.db.get(sql, openid=user_data.openid)
    #         if sql_user.open_id is None:
    #             flag = True
    #         else:
    #             flag = False
    #         self.render('home.html', flag=flag, user=user_data, sqluser=sql_user)
    @tornado.gen.coroutine
    def get(self):
        code = self.get_argument("code")
        client = AsyncHTTPClient()
        url = "https://api.weixin.qq.com/sns/oauth2/access_token?" \
              "appid=%s&secret=%s&code=%s&grant_type=authorization_code" % (
                  constants.WECHAT_APPID, constants.WECHAT_APPSECRET, code)
        resp = yield client.fetch(url)
        dict_data = json.loads(resp.body.decode('utf-8'))
        if "errcode" in dict_data:
            self.write("error occur")
        else:
            access_toke = dict_data["access_token"]
            open_id = dict_data["openid"]
            url = "https://api.weixin.qq.com/sns/userinfo?" \
                  "access_token=%s&openid=%s&lang=zh_CN" % (access_toke, open_id)
            resp = yield client.fetch(url)
            user_data = json.loads(resp.body.decode('utf-8'))

            sql = 'select wx_name, name, idcard, open_id, phone, xq_name, xq_louhao, xq_address, wx_head_image from t_user_info where open_id=%(openid)s'
            sql_user = self.db.get(sql, openid=open_id)
            if sql_user is None:
                flag = True
                sql_user = {
                    "id": None,
                    'wx_name ': None,
                    'name': None,
                    'idcard': None,
                    "open_id": None,
                    'phone': None,
                    'xq_name': None,
                    'xq_louhao': None,
                    'xq_address': None,
                    "wx_head_image": None,
                }
            else:
                flag = False
            self.render('home.html', flag=flag, user=user_data, sqluser=sql_user)

            # token = yield AccessToken.get_access_token()
            # temp_msg_url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s' % token
            # print(token)
            # c = AsyncHTTPClient()
            # data = {
            #     "touser": open_id,
            #     "template_id": "P6f7Ms9LE5UuHVyt-YP89NoOHYEy_aZeGVephrJVMs4",
            #     "url": "http://www.sougou.com",
            #     "data": {
            #         "first": {
            #             "value": "恭喜你购买成功！",
            #             "color": "#173177"
            #         },
            #         "product": {
            #             "value": "巧克力",
            #             "color": "#173177"
            #         },
            #         "price": {
            #             "value": "39.8元",
            #             "color": "#173177"
            #         },
            #         "time": {
            #             "value": "2014年9月22日",
            #             "color": "#173177"
            #         },
            #         "remark": {
            #             "value": "欢迎再次购买！",
            #             "color": "#173177"
            #         }
            #     }
            # }
            # data1 = {
            #     "touser": "oYXRo02MSCX-LCw4odGx1Wtq6UWo",
            #     "url": "http://www.sougou.com",
            #     "template_id": "P6f7Ms9LE5UuHVyt-YP89NoOHYEy_aZeGVephrJVMs4",
            #     "data": {
            #         "first": {
            #             "value": "恭喜你购买成功！",
            #             "color": "#173177"
            #         },
            #         "product": {
            #             "value": "巧克力",
            #             "color": "#173177"
            #         },
            #         "price": {
            #             "value": "39.8元",
            #             "color": "#173177"
            #         },
            #         "time": {
            #             "value": "2014年9月22日",
            #             "color": "#173177"
            #         },
            #         "remark": {
            #             "value": "欢迎再次购买！",
            #             "color": "#173177"
            #         }
            #     }
            # }
            # if not open_id == 'oYXRo02MSCX-LCw4odGx1Wtq6UWo':
            #     req1 = HTTPRequest(url=temp_msg_url, method='POST', body=json.dumps(data1, ensure_ascii=False))
            #     yield c.fetch(req1)
            # req = HTTPRequest(url=temp_msg_url, method='POST', body=json.dumps(data, ensure_ascii=False))
            # yield c.fetch(req)
            # if "errcode" in user_data:
            #     self.write("error occur again")
            # else:
            #     self.render("home.html", user=user_data)


class ProfilesHandler(BaseHandles.BaseHandle):
    def get(self):
        # token = yield AccessToken.get_access_token()
        # temp_msg_url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s' % token
        # print(token)
        # c = AsyncHTTPClient()
        # data = {
        #     "touser": open_id,
        #     "template_id": "P6f7Ms9LE5UuHVyt-YP89NoOHYEy_aZeGVephrJVMs4",
        #     "url": "http://www.sougou.com",
        #     "data": {
        #         "first": {
        #             "value": "恭喜你购买成功！",
        #             "color": "#173177"
        #         },
        #         "product": {
        #             "value": "巧克力",
        #             "color": "#173177"
        #         },
        #         "price": {
        #             "value": "39.8元",
        #             "color": "#173177"
        #         },
        #         "time": {
        #             "value": "2014年9月22日",
        #             "color": "#173177"
        #         },
        #         "remark": {
        #             "value": "欢迎再次购买！",
        #             "color": "#173177"
        #         }
        #     }
        # }
        # data1 = {
        #     "touser": "oYXRo02MSCX-LCw4odGx1Wtq6UWo",
        #     "url": "http://www.sougou.com",
        #     "template_id": "P6f7Ms9LE5UuHVyt-YP89NoOHYEy_aZeGVephrJVMs4",
        #     "data": {
        #         "first": {
        #             "value": "恭喜你购买成功！",
        #             "color": "#173177"
        #         },
        #         "product": {
        #             "value": "巧克力",
        #             "color": "#173177"
        #         },
        #         "price": {
        #             "value": "39.8元",
        #             "color": "#173177"
        #         },
        #         "time": {
        #             "value": "2014年9月22日",
        #             "color": "#173177"
        #         },
        #         "remark": {
        #             "value": "欢迎再次购买！",
        #             "color": "#173177"
        #         }
        #     }
        # }
        # if not open_id == 'oYXRo02MSCX-LCw4odGx1Wtq6UWo':
        #     req1 = HTTPRequest(url=temp_msg_url, method='POST', body=json.dumps(data1, ensure_ascii=False))
        #     yield c.fetch(req1)
        # req = HTTPRequest(url=temp_msg_url, method='POST', body=json.dumps(data, ensure_ascii=False))
        # yield c.fetch(req)
        # print(user_data)
        # if "errcode" in user_data:
        #     self.write("error occur again")
        # else:
        #     self.render("home.html", user=user_data)
        self.render("home.html")
