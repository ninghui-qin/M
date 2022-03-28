# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/3/26  10:16 下午

import requests
from common.client import RequestClient


class BaseBuyerApi(RequestClient):
    # session=requests.session()
    buyer_token=''
    def __init__(self):
        super().__init__()
        # self.session=BaseBuyerApi.session
        # self.url=None
        # self.method=None
        self.host='http://www.mtxshop.com:7002'
        self.headers={
            'Authorization': BaseBuyerApi.buyer_token
        }
        # self.params=None
        # self.data=None
        # self.json=None
        # self.files=None
        # self.resp=None

    # def send(self,**kwargs):
    #     # 抽取时要注意，每个request的请求不一定会发送多少个参数
    #     # 可以使用不定长关键字参数来传
    #     if 'url' not in kwargs:
    #         kwargs['url']=self.url
    #     if 'method' not in kwargs:
    #         kwargs['method']=self.method
    #     if 'headers' not in kwargs:
    #         kwargs['headers']=self.headers
    #     if 'params' not in kwargs:
    #         kwargs['params']=self.params
    #     if 'data' not in kwargs:
    #         kwargs['data']=self.data
    #     if 'json' not in kwargs:
    #         kwargs['json']=self.json
    #     if 'files' not in kwargs:
    #         kwargs['files']=self.files
    #
    #     self.resp = self.session.request(**kwargs)
    #
    #     return self.resp

class BaseSellerApi:
    seller_token=''
    def __init__(self):
        super.__init__()
        self.host='http://www.mtxshop.com:7003'
        self.headers={
            'Authorization': BaseBuyerApi.seller_token
        }
