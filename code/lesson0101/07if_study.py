# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2021-12-26 15:22
# @Copyright：北京码同学

# 从控制台输入一个数字，打印出他是偶数或者奇数
# a = input('请输入你的数字:')
# a = int(a)
# # a%2==0 这个表达式可以判断出a是否是偶数
# # if...else...要么执行if里的代码，要么执行else里的代码
# # 在python里通常使用:来表示一个代码块
# # 如何判断好几条语句属于一个代码块呢，通过缩进来判断
# # 缩进通常是一个tab键或者4个空格
# if a%2 == 0:
#     print(f'{a}是偶数')
#     print('xxxxx')
# else:
#     print(f'{a}是奇数')
# print('判断结束')


# 从控制台上输入学员成绩，90分以上是优秀，80以上是良好，70以上是一般，60以上及格，其他不及格
score = int(input('请输入成绩:'))
# if...elif...elif..else 多条件的情况下，只要满足一个则其他条件不会再被执行
if score>=90:
    print('优秀')
elif score>=80:
    print('良好')
elif score>=70:
    print('一般')
elif score>=60:
    print('及格')
else:
    print('不及格')

# 如果有钱就可以上车，上车后如果有座位就可以坐下
money = 1 #这表示有钱
seat = 1 # 这表示有座位
if money==1:
    print('我上车了，看看有没有座位')
    if seat == 1:
        print('有座位，赶紧坐下')
    else:
        print('没座位，只能站着')
else:
    print('没钱，上不了车')

if money == 1:
    print('这里只有if')

# 从控制台输入季节名称，判断是哪个季节，并且输出，比如输入春天，那么就打印春