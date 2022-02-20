# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-01-09 15:24
# @Copyright：北京码同学

# 字典也可以用来存储多组数据
# 注意字典中存储的数据都是键值对形式
# username:shamo 冒号前面叫做key，冒号后面叫做value
# 字典是可以存储多组键值对数据的
# stu1_info = {'username':'张三','age':18,'phone':'19100001111'}
stu1_info = {}
# 添加数据
stu1_info['username'] = '张三' # 追加一组键值对，中括号里填写key值，等号后边是value值
stu1_info['age'] = 18
stu1_info['phone'] = '19100001111'
stu1_info['wx'] = 'wxhdhgsg'
print(stu1_info)
# 修改数据
stu1_info['username'] = '张三三' #如果中括号里key已经在字典中了，那么这一句就是修改替换，如果不在就是添加

# 获取数据
# 需要知道你要获取的数据key是什么
print(stu1_info['phone']) # 这种方式获取数据时，如果key不存在，则会报错KeyError
# # 使用get方法获取
# print(stu1_info.get('phone')) # 这种方式获取数据时，如果key不存在，不会报错，返回结果是None

# 删除数据
del stu1_info['wx']
print(stu1_info)
# stu1_info.clear()# 清空所有数据

# 字典中的key是唯一的，相同的key只能存在一组，后加的相同的key会顶掉原来的值


# 遍历
# 我想得到字典中所有的key值，并且逐个打印
for key in stu1_info.keys():
    print(key)
    print(f'{key}:{stu1_info.get(key)}')
# 我想得到字典中所有的value值，并且逐个打印
for value in stu1_info.values():
    print(value)

# 我想直接遍历所有的key和value
for key,value in stu1_info.items():
    print(f'{key}:{value}')

# 对列表去重(使用字典特性实现)
students = ['王五', '王五', '李思思', '张三','李思思','赵六','张三']
# 字典特性是他的key是唯一的
# 去重，去掉重复的数据，相同的只保留一个
# 遍历列表，将列表中的每一个数据当做字典的key，那么最终这个字典中的key就都是唯一的了
dict1 = {}
for name in students:
    dict1[name] = 0
print(dict1)
# 接下来只要得到这个字典的所有的key，将其转换成列表即可
print(dict1.keys())
print(list(dict1.keys()))
print(list(dict1.values()))

students = ['王五', '王五', '李思思', '张三','李思思','赵六','张三']
# 使用类型转换，将列表转换成set集合
print(set(students))
set1 = {1,2,6,4} # set集合是用来存储不同的多组数据的，set默认就不会存在相同的数据
print(type(set1))


# 对列表去重(使用字典特性实现)
students = ['王五', '王五', '李思思', '张三','李思思','赵六','张三']
# 统计上述列表中，每个数据出现的次数，并且输出每个数据对应的次数
# 一旦发现有对应关系的这种数据，我们用什么来表示他呢
# 王五:2 李思思:2 张三:2 赵六:1
dict1 = {}
# for name in students:
#     # 如果dict1中不存在这个数据，那么直接添加1次
#     # 如果dict1中存在这个数据，那么在原来的基础上增加1
#     if name in dict1: #判断key是否存在于字典中
#         dict1[name] += 1
#     else:
#         dict1[name] = 1
# print(dict1)

for name in students:
    dict1[name] = students.count(name)
print(dict1)


# 学员信息有姓名和成绩，现在有多个学员，通过计算得出全班的平均成绩和第一名的姓名

# 首先需要一个结构来存储学员信息
stu1 = {'username':'张三','score':80}
stu2 = {'username':'李四','score':90}
stu3 = {'username':'王五','score':60}
stu4 = {'username':'赵六','score':90}
# 多个学员使用什么结构来存储
students = [stu1,stu2,stu3,stu4]
# 先计算平均成绩，所有学员成绩之和除以学员数量
count = len(students) #列表长度代表学员总数量
# 累加所有成绩
sum = 0 #代表总成绩
for stu in students:
    # sum = sum + stu['score']
    sum += stu['score']
print(f'平均分是:{sum/count}')
# 第一名的姓名
# 先要计算出最高成绩是多少
max_score = 0
# 遍历所有学员，使用学员成绩和max_score进行对比，如果比max_score大，那么就将他的值赋值给max_score
for stu in students:
    if max_score<stu['score']:
        max_score = stu['score']
print(f'最大成绩是:{max_score}')

# 通过max_score再次遍历学员列表，对比max_score和学员成绩，如果一样，则说明该学员是第一名
for stu in students:
    if max_score == stu['score']:
        print(stu['username'])


"""
作业
1.给出一个字符串如"errtyasdd"，找到最后一个只出现一次的字符，并返回下标
2.有一个序列： 1/1,1/2,2/3,3/5,5/8,8/13...  计算这个序列前十项的和
"""




