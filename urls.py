import os
from handles import WechatHandle, MenuHandle, ProfileHandles
from handles.BaseHandles import StaticHandle

con_path = os.path.dirname(__file__)


urls = [
    (r'/wechat', WechatHandle.WechatHandle),
    (r'/menu', MenuHandle.AddMenu),
    (r'/wechat/profiles', ProfileHandles.ProfilesHandler),
    (r'/wechat/profile', ProfileHandles.ProfileHandler),
    (r'/deleteMenu', MenuHandle.DeleteMenu),
    (r'/(.*)', StaticHandle, {'path': os.path.join(con_path, 'static'), 'default_filename': 'home.html'}),
]