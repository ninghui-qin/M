# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/1/12  20:20 下午
"""
作业
1.给出一个字符串如"errtyasdd"，找到最后一个只出现一次的字符，并返回下标
2.有一个序列： 1/1,1/2,2/3,3/5,5/8,8/13...  计算这个序列前十项的和
"""
from functools import reduce

n=1 #n为分子
m=1 #m为分母
sum=1 #前n项和
for i in range(1,10):
    temp=m
    m=n+m
    n=temp
    sum +=n/m
    print(f'第{i+1}项的和为{sum}')


reduce
