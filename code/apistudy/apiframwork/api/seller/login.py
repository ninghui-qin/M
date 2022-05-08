# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/4/5  5:00 下午
from api.base_api import BaseSellerApi
from common.encry_decry import md5
from common.file_load import load_yaml_file


class SellerLogin(BaseSellerApi):

    def __init__(self):
        super().__init__()
        self.common = load_yaml_file('/config/common.yml')
        self.url = f'{self.host}/seller/login'
        self.method = 'get'
        self.params = {
            'username': self.common['sellerName'],
            'password': md5(self.common['sellerPassword']),
            'captcha': self.common['captcha'],
            'uuid': 'jsjdhdhdhdhdhdhh'
        }