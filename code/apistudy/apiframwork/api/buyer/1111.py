# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/3/26  11:39 下午
from api.base_api import BaseBuyerApi
from api.buyer.cart import AddCartApi, BuyNowApi
from api.buyer.login import BuyerLogin

if __name__ == '__main__':
    buyer_login=BuyerLogin()
    resp=buyer_login.send()
    BaseBuyerApi.token=resp.json()['access_token']
    add_cart=AddCartApi(sku_id=5173,num=1)
    resp=add_cart.send()
    # buy_now=BuyNowApi(sku_id=5173,num=1)
    # resp=buy_now.send()
    print(resp.json())