# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2021-12-26 11:43
# @Copyright：北京码同学

# 数据类型

age = 18 # int
# 如何查看一个变量的数据类型
age_type = type(age) # type这个函数可以获取某个变量的类型
print(age_type)
weight = 78.4 # float
print(type(weight))

# 布尔类型
# 布尔类型只有两个值，要么是True，要么是False
# 布尔类型通常用来存储生活中肯定或者否定的答案
flag = True # 肯定的，是，确定，同意
flag1 = False # 否定的，否，不确定，不同意，没吃饭，没听懂
print(type(flag))  # bool

# 字符串类型
name = '沙陌'
# 单引号表示字符串，双引号也表示字符串，三引号也可以表示字符串
school_name = "码同学"
# 有一定格式的字符串可以用三引号来处理
# 比如一首诗
shi = """
白日依山尽,
黄河入海流。
欲穷千里目,
更上一层楼。
"""
print(shi)
# 如果说你的字符串不需要固定的格式，那么推荐使用单引号
print('"这是外面套的单引号"')
print("'这是外面套的双引号'")

# 上述几种变量类型都只能存储单一的数据类型
# 如果要存储多个数据，那么可以采用列表进行存储
i_like_nv_star = ['赵丽颖','高圆圆','青鸟']
# 列表可以存储不同类型的数据
list1 = ['sss',True,18,19.7]
print(type(list1))#list


#元组
tuple1 = ('shsh',17,89.5)
print(type(tuple1)) #tuple

# {'username':'shamo','age':18,'job':'tester'}
# 使用字典来表示上述数据形式
# 字典是用来存储多组键值对形式的数据
# 冒号前面是key，也就是键
# 冒号后面是value，也就是值
user = {'username':'shamo','age':18,'job':'tester'}
print(type(user)) #dict
print('判断user变量是否是字典类型:{}'.format(isinstance(user,dict))) #判断user变量是否是字典类型
print(isinstance(tuple1,dict)) #判断tuple1变量是否是字典类型