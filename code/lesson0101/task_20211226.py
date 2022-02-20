# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2021/12/26  10:32 下午


# 1. 从控制台输入年、月、日，计算输入的日期，是这一年的第几天
# 比如2021.2.18 ,是2021年的第49天
# 比如2021.4.7,是2021年的第97天

'''
1.判断year是否为闰年，year%4==0
2.若是闰年，则用
'''
date=input('请输入时间（如20211229）：')
year=int(date[0:4])
month=int(date[4:6])
day=int(date[6:8])
n=0  #n+day是要的答案
x=0  #x是2月份的天数

if year%4==0:
    x=29
else:
    x=28
num1=[0,31,x,31,30,31,30,31,31,30,31,30,31]

i=0
while i<month:
    n+=num1[i]
    print(f'x={x},i={i},n={n}')
    i+=1
print(f'{date}是{year}年的第{n+day}天')
