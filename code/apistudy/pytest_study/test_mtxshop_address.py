# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/3/26  2:00 下午
import javaobj
import pytest
from requests_study.mtxshop_api import set_address, set_payment_type
class TestSetAddress:
    def test_set_address(self,redis_util,get_token): # 调用接口拿到返回
        resp = set_address()
        status_code = resp.status_code
        assert status_code == 200
        resp = set_payment_type()
        status_code = resp.status_code
        assert status_code == 200
        uid = get_token # get_token是个fixture，调用时他就相当于他的返回值，我们返回了
        res = redis_util.get(f'{{CHECKOUT_PARAM_ID_PREFIX}}_{uid}') # res是个字典
        for key, value in res.items():
            key = javaobj.loads(key)
            try:
                value = javaobj.loads(value)
                if key == 'addressId':
                    pytest.assume(value==3896)
                if key == 'paymentType':
                    value = value.__getattribute__('constant')
                    pytest.assume(value=='COD')
            except:
                pass