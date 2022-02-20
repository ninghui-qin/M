# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-01-16 14:42
# @Copyright：北京码同学

# 几个高阶函数，了解下，主要是做面试题的时候可能会用到

# 计算给定序列中各个数字的2次方,生成一个新的列表
from functools import reduce

list1 = [2,4,6,7,2,6] # 新的是[4,16,36,49,4,36]

def ercifang(i):
    return i**2
# map(ercifang, list1) 含义是，将list1中的每个数据传递给函数ercifang进行计算，得到新结果
print(list(map(ercifang, list1)))
# 使用匿名函数
print(list(map(lambda i:i**2, list1)))
list2 = ['20cm','10mm','30mm','50cm','70cm']
# 提出list2这个列表中以cm结尾数据，形成新的列表
def jduge_cm(i:str): #i:str  注意这是声明入参的类型是字符串
    if i.endswith('cm'):
        return i
print(list(map(jduge_cm, list2)))


# 计算一个列表的所有项的乘几
list3 = [2,4,6,7,2,6]
# 需要导入from functools import reduce
print(reduce(lambda x, y: x * y, list3))

# 得到一个列表中所有的偶数
list4 = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x: x % 2 == 0, list4)))

list5 = ['20cm','10mm','30mm','50cm','70cm']
# 提出list2这个列表中以cm结尾数据，形成新的列表
def jduge_cm(i:str): #i:str  注意这是声明入参的类型是字符串
    return i.endswith('cm')
print(list(filter(lambda i: i.endswith('cm'), list5)))
print(list(filter(jduge_cm, list5)))
#filter 的第一个参数是函数，这个函数的返回值是布尔值，表示是否满足条件