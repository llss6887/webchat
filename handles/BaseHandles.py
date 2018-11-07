# coding:utf-8

from tornado.web import StaticFileHandler, RequestHandler


class BaseHandle(RequestHandler):

    @property
    def db(self):
        return self.application.db


class StaticHandle(StaticFileHandler):
    def __init__(self, *args, **kwargs):
        super(StaticHandle, self).__init__(*args, **kwargs)
        self.xsrf_token