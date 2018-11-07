# coding:utf-8

import os

setting = dict(
        static_path=os.path.join(os.path.dirname(__file__), 'static'),
        template_path=os.path.join(os.path.dirname(__file__), "template"),
        cookie_secret='880LoMfQTP6ZcgPpiNiXdvsLOdT4pU2YrADi073wOdI=',
        xsrf_cookies=True,
        debug=True
)

mysql_options = dict(
    host='182.61.48.80',
    database='wechat',
    user='root',
    password='root'
)

log_path = os.path.join(os.path.dirname(__file__), 'logs/log')
log_level = 'debug'

passwd_hash_key = "nlgCjaTXQX2jpupQFQLoQo5N4OkEmkeHsHD9+BBx2WQ="