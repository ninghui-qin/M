# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/1/16  3:29 下午
import os

f=open('text.txt','a')
# f.write('第一行在这里哦\n'
#         '第二行在这里哦\n'
#         '第三行了哦\n'
#         '第四行了啦\n')

f.close()


with open('../lesson0109/text.txt','r') as f:
        print(f.readlines())

print(os.path.dirname(__file__))

if os.path.exists('/Users/ninghui/PycharmProjects/pythonProject/base/lesson0109/text.txt'):
        print('存在')
else:
        print('不存在')

