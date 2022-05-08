# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/4/5  9:23 下午
from api.base_api import BaseSellerApi


class OrderDeliveryApi(BaseSellerApi):

    def __init__(self,order_sn):
        super().__init__()
        self.url = f'{self.host}/seller/trade/orders/{order_sn}/delivery'
        self.method = 'post'
        self.params = {
            'ship_no':'assdfddfg',
            'logi_id':12,
            'logi_name':'中通'
        }
class OrderPayApi(BaseSellerApi):

    def __init__(self,order_sn,pay_price):
        super().__init__()
        self.url = f'{self.host}/seller/trade/orders/{order_sn}/pay'
        self.method = 'post'
        self.params = {
            'pay_price':pay_price
        }