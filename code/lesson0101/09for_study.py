# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2021-12-26 16:52
# @Copyright：北京码同学

s = 'shamo'
# 逐个输出s这个字符串里的每一个字符
# print('s')
# print('h')
# print('a')
# in后面跟的是一个序列，序列最简单的理解就是一个有序的排列
# c在这里是一个临时的变量，他用来在每次循环时接收s里边的字符
for c in s:
    print(c)

#使用for循环来实现1-100之间的数字和
# range(100) #这会生成0-100之间的序列，不包括100
sum = 0
# for i in range(100):
#     sum =sum+i
# print(sum)
#使用for循环来实现88-198,包括198,之间的数字和
for i in range(88,199):
    if i == 133:
        break
    sum = sum + i
else:
    # 如果循环被break终止了，那么else里的代码不会被执行
    # 但是如果是continue，else里的代码是会被执行的
    print(f'循环正常结束之后结果是:{sum}')
print('不管上面的循环是否正常结束，我都会执行sum的结果:{}'.format(sum))

like_star = ['赵丽颖','高圆圆','白露']
for name in like_star:
    print(name)
# print(name)

# 今天的作业:
# 1. 从控制台输入年、月、日，计算输入的日期，是这一年的第几天
# 比如2021.2.18 ,是2021年的第49天
# 比如2021.4.7,是2021年的第97天
