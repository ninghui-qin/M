# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/3/26  10:02 下午
import requests

from api.base_api import BaseBuyerApi


class AddCartApi(BaseBuyerApi):

    def __init__(self,sku_id,num):
        super().__init__()

        self.url = 'http://www.mtxshop.com:7002/trade/carts'
        # global token
        # self.headers = {
        #     'Authorization': token
        # }
        self.method='post'
        self.params = {
            'sku_id': sku_id,
            'num': num
        }
    # def send(self):
    #     resp = requests.session.request(url=self.url, method='post', headers=self.headers, params=self.params)
    #     return resp

class BuyNowApi(BaseBuyerApi):


    def __init__(self,sku_id,num):
        super().__init__()

        self.url = f'{self.host}/trade/carts/buy'
        # global token
        # self.headers = {
        #     'Authorization': token
        # }
        self.method='post'
        self.params = {
            'sku_id': sku_id,
            'num': num
        }
    #
    # def send(self):
    #     resp = requests.session.request(url=self.url, method='post', headers=self.headers, params=self.params)
    #     return resp

class DeleteCartApi(BaseBuyerApi):

    def __init__(self):
        super().__init__()

        self.url = f'{self.host}/trade/carts'
        # global token
        # self.headers = {
        #     'Authorization': token
        # }
        self.method='delete'
    #
    # def send(self):
    #     resp = requests.session.request(url=self.url, method='delete', headers=self.headers)
    #     return resp