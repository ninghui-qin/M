# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/4/5  9:48 下午

from api.base_api import BaseManagerApi


class AuditGoodsApi(BaseManagerApi):

    # 注意该参数goods_id要求是一个列表
    def __init__(self,goods_ids:list):
        super().__init__()
        self.url = f'{self.host}/admin/goods/batch/audit'
        self.method = 'post'
        self.json = {
            "goods_ids": goods_ids,
            "message": "aaaa",
            "pass": 1
        }