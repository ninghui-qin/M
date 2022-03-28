# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/3/5  4:06 下午

import requests
from db import *
from mtxshop_api import *

session = requests.session()
token = ''


def seller_login():
    '''卖家登录'''
    url='http://www.mtxshop.com:7003/seller/login'
    headers = {
        'Authorization': ''
    }
    data={
        'username':'shamoseller',
        'password':'e10adc3949ba59abbe56e057f20f883e',
        'captcha':'1512',
        'uuid':'74f35140-9578-11ec-af73'
    }
    resp=session.request(url=url,method='get',params=data)
    resp_json=resp.json()
    # print(resp_json)
    global token
    token=resp_json['access_token']
    return resp

def add_goods():
    '''添加商品'''
    url='http://www.mtxshop.com:7003/seller/goods'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    data={
  "brand_id": 444,
  "category_id": 1,
  "category_name": "hiahia",
  "cost": 0,
  "exchange": {
    "category_id": 0,
    "enable_exchange": 0,
    "exchange_money": 0,
    "exchange_point": 0
  },
  "goods_gallery_list": [
    {
      "img_id": 67,
      "original": "https://huotan-img.azz.net/image/2021/10/31/19/5_54a81e7d05.jpg",
      "sort": 5
    }
  ],
  "goods_name": "wlop",
  "goods_params_list": [
    {
      "param_id": 2,
      "param_name": "wlopp",
      "param_value": "333"
    }
  ],
  "goods_transfee_charge": 0,
  "has_changed": 0,
  "intro": "3333",
  "market_enable": 0,
  "meta_description": "333333333",
  "meta_keywords": "33333",
  "mktprice": 0,
  "page_title": "33333",
  "price": 0,
  "quantity": 0,
  "shop_cat_id": 0,
  "sku_list": [
    {
      "cost": 0,
      "enable_quantity": 0,
      "goods_type": "333333",
      "price": 0,
      "quantity": 0,
      "sn": "33333333",
      "spec_list": [
        {
          "spec_id": 0,
          "spec_image": "https://huotan-img.azz.net/image/2021/10/31/19/5_54a81e7d05.jpg",
          "spec_name": "wlop",
          "spec_type": 0,
          "spec_value": "3333",
          "spec_value_id": 0
        }
      ],
      "template_id": 0,
      "weight": 0
    }
  ],
  "sn": "33333333",
  "template_id": 0,
  "weight": 0
    }
    resp = session.request(url=url,method='post', headers=headers, json=data)
    resp_json=resp.json()
    # print(resp_json)
    return resp

def change_goods(goods_id=6992):
    '''修改商品信息'''
    url = f'http://www.mtxshop.com:7003/seller/goods/{goods_id}'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    data ={
    "goods_id":6975,
    "category_id":1,
    "category_name":"食品饮料",
    "shop_cat_id":0,
    "brand_id":444,
    "goods_name":"wlop",
    "sn":"33333333",
    "price":"33",
    "cost":"33",
    "mktprice":"33",
    "weight":"3",
    "goods_transfee_charge":1,
    "intro":"<p>3333</p>",
    "have_spec":1,
    "quantity":0,
    "market_enable":1,
    "goods_gallery_list":[
        {
            "img_id":9220,
            "original":"https://huotan-img.azz.net/image/2021/10/31/19/5_54a81e7d05.jpg",
            "sort":666
        }
    ],
    "page_title":"33333",
    "meta_keywords":"33333",
    "meta_description":"333333333",
    "template_id":0,
    "is_auth":0,
    "enable_quantity":0,
    "auth_message":6666,
    "goods_type":"NORMAL",
    "exchange":{
        "category_id":"",
        "enable_exchange":0,
        "exchange_money":0,
        "exchange_point":0
    },
    "category_ids":[
        1
    ],
    "promotion_tip":"",
    "sku_list":[

    ],
    "goods_params_list":[
        {
            "id":666,
            "goods_id":666,
            "param_id":231,
            "param_name":"生产许可证编号",
            "param_value":"",
            "param_type":1,
            "options":"",
            "required":0,
            "group_id":51,
            "is_index":0,
            "option_list":[
                ""
            ]
        }
    ],
    "has_changed":0
    }
    resp = session.request(url=url, method='put', headers=headers, json=data)
    resp_json = resp.json()
    # print(resp_json)
    return resp

def delivery(order_sn,ship_no='12345699999999',logi_id=13,logi_name='balala'):
    '''发货'''
    url = f'http://www.mtxshop.com:7003/seller/trade/orders/{order_sn}/delivery'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    data={
        'ship_no':ship_no,
        'logi_id':logi_id,
        'logi_name':logi_name
    }
    resp = session.request(url=url, method='post', headers=headers, params=data)
    print(resp.status_code)
    # print(order_sn)
    # if ship_no=='':
    #     print(resp)
    if logi_id=='':
        print(resp.json())
    elif logi_name=='':
        print(resp)
    return resp

def pay():
    '''确认收款'''
    result = DB().select(
        "SELECT trade_sn,order_price from mtxshop_trade.es_order where seller_id=20 and order_status like 'ROG' order by create_time desc limit 10;")
    order_sn=result[0]['trade_sn']
    pay_price=result[0]['order_price']

    url = f'http://www.mtxshop.com:7003/seller/trade/orders/{order_sn}/pay'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    data = {
        'pay_price': pay_price
    }
    resp = session.request(url=url, method='post', headers=headers, params=data)
    # print(resp.status_code)
    return resp



if __name__ == '__main__':
    seller_login()
    # add_goods()
    # change_goods()
    order=DB().select("SELECT trade_sn from mtxshop_trade.es_order where seller_id=20 and order_status like 'CONFIRM' order by create_time desc limit 10;")
    order_sn=order[0]['trade_sn']
    delivery(order_sn,ship_no='',logi_id='',logi_name='balala')
    # pay()
