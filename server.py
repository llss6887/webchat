# coding:utf-8

import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options, define
import config
from urls import urls
from util import tornadb

define('port', default=80, type=int, help='run server on the given port')


class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.db = tornadb.Connection(**config.mysql_options)


def main():
    options.log_file_prefix = config.log_path
    options.logging = config.log_level
    options.parse_command_line()

    app = Application(
        urls,
        **config.setting
    )
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
