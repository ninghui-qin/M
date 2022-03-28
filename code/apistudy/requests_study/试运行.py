# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/3/20  9:20 下午

import javaobj
import pytest
from requests_study.db import *
from requests_study.seller_api import *

def setup_module():
    seller_login()

db=DB()
order_sn=[]
order_status=['CONFIRM','SHIPPED','ROG','PAID_OFF','COMPLETE','CANCELLED']
for i in order_status:
    sql=f"SELECT trade_sn from mtxshop_trade.es_order where seller_id=20 and order_status = '{i}' order by create_time desc limit 10;"
    db = DB()
    dbdata=db.select(sql)
    # print(dbdata)
    order_sn.append(dbdata[0]['trade_sn'])
print(order_sn)