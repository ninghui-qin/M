# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/4/5  4:58 下午
from api.base_api import BaseBuyerApi


class CommentApi(BaseBuyerApi):

    def __init__(self,order_sn,sku_id):
        super().__init__()
        self.url = f'{self.host}/members/comments'
        self.method = 'post'
        self.json = {
            "order_sn": order_sn,
            "delivery_score": 5,
            "description_score": 5,
            "service_score": 5,
            "comments": [{
                "sku_id": sku_id,
                "content": "这就是个评论，不要管我说啥",
                "grade": "good",
                "images": []
            }]
        }