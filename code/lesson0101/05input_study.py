# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2021-12-26 14:00
# @Copyright：北京码同学

# input这个函数仅仅只是为了和控制台上进行交互

# name = 'shamo'
name = input('请输入你的姓名:')
print('从控制台上输入的姓名是:{}'.format(name))
age = input('请输入你的年龄:') #注意，input函数从控制台上得到的都是字符串类型
print(type(age))
# 将上面得到的age变量转换成数字类型
age = int(age) #先把age变量转型成int类型，再把他赋值给age变量
print(f'转换后的age类型是:{type(age)}')

weight = '78.5' #这是一个字符串类型的小数
weight = float(weight)
print(f'字符串小数转换后是{type(weight)}')

height = 178
height = str(height)
print(f'数字转换成字符串后类型是:{type(height)}')

# 当你的字符串型的数字最前面是0时，转换成数字后0会被省略掉
a = '0089'
a = int(a)
print(a)

s = 'abc' # 这种是无法转换成数字，因为他本身不是数字
print(int(s))