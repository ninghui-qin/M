# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/3/27  4:15 下午

import os

ABS_PATH = os.path.abspath(__file__) #获取当前文件的绝对路径
DIR_NAME = os.path.dirname(ABS_PATH) #获取文件所在的目录

# print(ABS_PATH)
# print(DIR_NAME)
print(DIR_NAME)
print(type(DIR_NAME))