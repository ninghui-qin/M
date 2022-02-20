# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/1/12  20:43 下午
"""
作业
1.给出一个字符串如"errtyasdd"，找到最后一个只出现一次的字符，并返回下标
2.有一个序列： 1/1,1/2,2/3,3/5,5/8,8/13...  计算这个序列前十项的和
"""
# str1="errtyasdd"
str1=input('请随便输入：')
list1=list(str1)
list1.reverse()
# print(list1)
for i in list1:
    # print(f'当前i={i},出现的次数为{list1.count(i)}')
    if list1.count(i) == 1:
        list1.reverse()
        print(f'最后一个只出现一次的字符为：{i}，下标为：{list1.index(i)}')
        break
