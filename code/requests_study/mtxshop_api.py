# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-02-20 17:14
# @Copyright：北京码同学
import requests

session = requests.session()
token = ''
def buyer_login():
    url = 'http://www.mtxshop.com:7002/passport/login'

    headers = {
        'Authorization': ''
    }
    # 查询参数通常使用params来表示
    params = {
        'username': 'shamo',
        'password': 'e10adc3949ba59abbe56e057f20f883e',
        'captcha': '1512',
        'uuid': 'jsjdhdhdhdhdhdhh'
    }
    resp = session.request(url=url,method='post', headers=headers, params=params)

    status_code = resp.status_code  # 获取响应状态码
    # print(status_code)
    # resp_info = resp.text  # 获取响应信息，返回结果是字符串格式
    resp_json = resp.json()  # 获取响应信息，返回结果是个字典，注意这种方法只能针对响应信息是json格式
    # print(resp_info)
    print(resp_json)
    global token
    token = resp_json['access_token']
def add_cart():
    url = 'http://www.mtxshop.com:7002/trade/carts'
    global token
    headers = {
        'Authorization': token
    }
    # 查询参数通常使用params来表示
    params = {
        'sku_id': 5173,
        'num': 1
    }
    resp = session.request(url=url,method='post', headers=headers, params=params)

    status_code = resp.status_code  # 获取响应状态码
    # print(status_code)
    # resp_info = resp.text  # 获取响应信息，返回结果是字符串格式
    resp_json = resp.json()  # 获取响应信息，返回结果是个字典，注意这种方法只能针对响应信息是json格式
    # print(resp_info)
    print(resp_json)
if __name__ == '__main__':
    buyer_login()
    add_cart()