# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/4/5  9:52 下午
from api.base_api import BaseBasicApi
from setting import DIR_NAME


class UploadFileApi(BaseBasicApi):

    def __init__(self):
        super().__init__()
        self.host=f'{self.host}/uploaders'
        self.method='post'
        self.files = {
            # 'logo.png' 文件名称
            # open(r'C:\Users\lixio\Desktop\logo.png',mode='rb')  读取文件二进制对象
            # 'image/png' 文件类型
            'file':('logo.png',open(DIR_NAME+'/data/logo.png',mode='rb'),'image/png')
        }
        self.params={
            'scence':'goods'
        }

if __name__ == '__main__':
    resp=UploadFileApi().send()
    print(resp.status_code)
    print(resp.json())