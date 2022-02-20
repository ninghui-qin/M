# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-01-16 15:19
# @Copyright：北京码同学

# 文件操作

# 写文件
# 文件路径
# mode表示的是针对这个文件要做什么操作，w表示覆盖写入
# encoding是指定写入时的编码
# 写文件时不会判断文件是否存在，如果没有就先创建，如果有就直接写
# f = open('test.txt',mode='w',encoding='UTF-8')
# f.write('沙陌你好1')
# f.close()

# 我想实现追加写入,mode=a表示追加
# f = open('test.txt',mode='a',encoding='UTF-8')
# f.write('沙陌你好1')
# f.close()
# 生成大量文件、
# for i in range(10):
#     f = open(f'test{i}.txt',mode='a',encoding='UTF-8')
#     f.write('沙陌你好1')
#     f.close()


# 读文件
# 文件不存在时会报错FileNotFoundError: [Errno 2] No such file or directory: 'test1.txt'
import os

f = open('test.txt',mode='r',encoding='UTF-8')
# 沙陌你好1沙陌你好1沙陌你好1沙陌你好1沙陌你好1
# print(f.read(2)) #里边的数字指的字符数
# print(f.read(3))
# print(f.readline()) #不写参数的话就是读整行
# print(f.readline(4))
print(f.readlines())
# print(f.readlines(28))
f.close()


# 读和写另外一种方式
with open('test.txt',mode='a',encoding='UTF-8') as f:
    f.write('这是新写的')

with open('test.txt',mode='r',encoding='UTF-8') as f:
    print(f.readlines())

# 相对路径
with open('../lesson1226/test1226.txt',mode='r',encoding='UTF-8') as f:
    print(f.readlines())

# D:\pycharmprojects\python1226\pythonbasic\lesson1226\test1226.txt
with open(r'D:\pycharmprojects\python1226\pythonbasic\lesson1226\test1226.txt',mode='r',encoding='UTF-8') as f:
    print(f.readlines())


print(os.path.dirname(__file__))
print(os.path.abspath(__file__))
if os.path.exists(r'D:\pycharmprojects\python12261\pythonbasic\lesson1226\test1226.txt'):
    print('存在')
else:
    print('不存在')