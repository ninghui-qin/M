# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/4/5  5:00 下午
from api.base_api import BaseManagerApi
# from common.encry_decry import md5
# from common.file_load import load_yaml_file


class ManagerLogin(BaseManagerApi):

    def __init__(self):
        super().__init__()
        self.common = f'{self.host}/admin/systems/admin-users/login'
        self.url = f'{self.host}/seller/login'
        self.method = 'get'
        self.params = {
            'username': 'admin',
            'password': '96e79218965eb72c92a549dd5a330112',
            'captcha': '1512',
            'uuid': 'jsjdhdhdhdhdhdhh'
        }