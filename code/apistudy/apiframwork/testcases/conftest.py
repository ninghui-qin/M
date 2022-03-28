# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/3/26  9:36 下午
import pytest

from api.base_api import BaseBuyerApi
from api.buyer.login import BuyerLogin


@pytest.fixture(scope='session',autouse=True)
def get_buyer_token():
    buyer_login=BuyerLogin()
    resp=buyer_login.send()
    BaseBuyerApi.buyer_token=resp.json()['access_token']
