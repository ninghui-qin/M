# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2021/12/30  9:47 下午
'''
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j or j!=k:
                print(i,j,k)
print(f'共有{4*3*2}中组合')