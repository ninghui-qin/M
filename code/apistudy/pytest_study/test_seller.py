# # !/usr/bin python3.8
# # encoding: utf-8 -*-
# # @author: ninghui_hiahia
# # @Time: 2022/3/14  12:26 上午
# import javaobj
# import pytest
# from requests_study.db import *
# from requests_study.seller_api import *
#
# def setup_module():
#     seller_login()
# class TestDelivery:
#     order_sn=['']
#     order_status=['NEW','CONFIRM','SHIPPED','ROG','PAID_OFF','COMPLETE','CANCELLED']
#     for i in order_status:
#         sql=f"SELECT trade_sn from mtxshop_trade.es_order where seller_id=20 and order_status like '{i}' order by create_time desc limit 10;"
#         db = DB()
#         dbdata=db.select(sql)
#         order_sn.append(dbdata[0]['trade_sn'])
#     ship_no=['123','']
#     logi_id=['1','10','']
#     logi_name=['中通','']
#     expect_status_code=[200,500]
#     @pytest.mark.parametrize('order_sn',order_sn)
#     @pytest.mark.parametrize('ship_no',ship_no)
#     @pytest.mark.parametrize('logi_id',logi_id)
#     @pytest.mark.parametrize('logi_name',logi_name)
#     @pytest.mark.parametrize('expect_status_code',logi_name)
#     def test_delivery(self,order_sn,ship_no,logi_id,logi_name):