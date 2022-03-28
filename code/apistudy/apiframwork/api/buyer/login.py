# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/3/26  9:57 下午

import requests

from apiframwork.api.base_api import BaseBuyerApi


class BuyerLogin(BaseBuyerApi):

    def __init__(self):
        super().__init__()

        self.url = f'{self.host}/passport/login'

        # self.headers = {
        #     'Authorization': ''
        # }
        self.method='post'
        self.params = {
            'username': 'shamo',
            'password': 'e10adc3949ba59abbe56e057f20f883e',
            'captcha': '1512',
            'uuid': 'jsjdhdhdhdhdhdhh'
        }

    # def send(self):
    #     resp = requests.session.request(url=self.url, method='post', headers=self.headers, params=self.params)
    #     return resp
    #     status_code = resp.status_code  # 获取响应状态码
