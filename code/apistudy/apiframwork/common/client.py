# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/3/27  12:08 上午
import requests

from common.logger import GetLogger


class RequestClient:

    session=requests.session()
    def __init__(self):
        self.logger=GetLogger.get_logger()
        self.session=RequestClient.session
        self.url=None
        self.method=None
        self.headers=None
        self.params=None
        self.data=None
        self.json=None
        self.files=None
        self.resp=None

    def send(self,**kwargs):
        # 抽取时要注意，每个request的请求不一定会发送多少个参数
        # 可以使用不定长关键字参数来传
        if 'url' not in kwargs:
            kwargs['url']=self.url
        if 'method' not in kwargs:
            kwargs['method']=self.method
        if 'headers' not in kwargs:
            kwargs['headers']=self.headers
        if 'params' not in kwargs:
            kwargs['params']=self.params
        if 'data' not in kwargs:
            kwargs['data']=self.data
        if 'json' not in kwargs:
            kwargs['json']=self.json
        if 'files' not in kwargs:
            kwargs['files']=self.files

        for key,value in kwargs.items():
            self.logger.debug(f'接口的{key}是：{value}')
        try:
            self.resp = self.session.request(**kwargs)
            self.logger.debug(f'接口的响应状态码是{self.resp.status_code}')
            self.logger.debug(f'接口的响应是{self.resp.text}')
        except:
            self.logger.exception('接口发起异常')
        return self.resp