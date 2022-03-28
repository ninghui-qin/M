# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/3/27  12:38 上午
from api.base_api import BaseBuyerApi


class CreateTradeApi(BaseBuyerApi):
    def __init__(self,client='PC',way='BUY_NOW'):
        super.__init__()
        self.url=f'{self.host}/trade/create'
        self.method='post'
        self.params={
            'client':client,
            'way':way
        }