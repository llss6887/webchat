# coding=utf-8
import time
from hashlib import sha1
import xmltodict
import constants
from handles import BaseHandles


class WechatHandle(BaseHandles.BaseHandle):
    def prepare(self):
        signature = self.get_argument("signature")
        timestamp = self.get_argument("timestamp")
        nonce = self.get_argument("nonce")
        data = [constants.WECHAT_TOKEN, timestamp, nonce]
        data.sort()
        data = ''.join(data)
        real_signature = sha1(data.encode('utf-8')).hexdigest()
        if real_signature != signature:
            self.send_error(403)

    def get(self):
        echostr = self.get_argument('echostr')
        self.write(echostr)

    def post(self):
        xml_data = self.request.body
        dict_data = xmltodict.parse(xml_data)
        msg_type = dict_data['xml']['MsgType']
        if msg_type == 'text':
            content = dict_data["xml"]["Content"]
            resp_data = {
                "xml":{
                    "ToUserName": dict_data["xml"]["FromUserName"],
                    "FromUserName": dict_data["xml"]["ToUserName"],
                    "CreateTime": int(time.time()),
                    "MsgType": "text",
                    "Content": content,
                }
            }
            self.write(xmltodict.unparse(resp_data))
        elif msg_type == "event":
            if dict_data["xml"]["Event"] == "subscribe":
                """用户关注的事件"""
                resp_data = {
                    "xml": {
                        "ToUserName": dict_data["xml"]["FromUserName"],
                        "FromUserName": dict_data["xml"]["ToUserName"],
                        "CreateTime": int(time.time()),
                        "MsgType": "text",
                        "Content": u"您来啦，笑而不语",
                    }
                }
                if "EventKey" in dict_data["xml"]:
                    event_key = dict_data["xml"]["EventKey"]
                    resp_data["xml"]["Content"] = u"您来啦，笑而不语"
                self.write(xmltodict.unparse(resp_data))
            elif dict_data["xml"]["Event"] == "CLICK":
                # content = '你好，欢迎点获取'
                # resp_data = {
                #     "xml": {
                #         "ToUserName": dict_data["xml"]["FromUserName"],
                #         "FromUserName": dict_data["xml"]["ToUserName"],
                #         "CreateTime": int(time.time()),
                #         "MsgType": "text",
                #         "Content": content,
                #     }
                # }
                resp_data = {
                    "xml": {
                        "ToUserName": dict_data["xml"]["FromUserName"],
                        "FromUserName": dict_data["xml"]["ToUserName"],
                        "CreateTime": int(time.time()),
                        "MsgType": "news",
                        "ArticleCount": 1,
                        "Articles": {
                            "item": {
                                "Title": "第一个图文消息",
                                "Description": "这是我的第一个图文消息",
                                "PicUrl": "http://vip.n168.com/uploads/z/zmenyt1414119303/5/1/d/7/5580eaa73cc19.jpg",
                                "Url": "www.baidu.com",
                            }
                            # ,
                            # "item": {
                            #     "Title": "第二个图文消息",
                            #     "Description": "这是我的第一个图文消息",
                            #     "PicUrl": "http://images2015.cnblogs.com/blog/785499/201603/785499-20160308110435429-590906761.png",
                            #     "Url": "www.sougou.com",
                            # }
                        }
                    }
                }
                self.write(xmltodict.unparse(resp_data))
