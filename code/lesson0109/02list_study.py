# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-01-09 13:40
# @Copyright：北京码同学

# 列表 主要用来存储多组数据
students = [] #定义一个空列表
# students = ['张三','李四','王五'] #定义一个有数据的列表
# 向列表追加数据，在列表末尾
students.append('张三')
students.append('李四')
print(students)
students.append('王五')
print(students)
# 向列表插入数据，指定插入位置，这个位置是索引值
students.insert(1,'赵六')
print(students)

# 获取列表数据
# 我想知道第三个学员是谁
print(students[2])
# 我想知道最后三个学员
print(students[1:])
print(students[-3:])

# 我要修改第2个学员的姓名
students[1] = '李思思'
print(students)

# 删除列表数据
del students[2]
print(students)

# 列表长度获取，或者说列表数据个数
print(len(students))

# 判断列表是否存在某个数据
print('李思思' in students) #存在返回True，不存在返回False

# 我想知道某个数据的位置
print(students.index('王五'))

# 统计某个数据存在的次数
students.append('王五')
print(students.count('王五'))

# 列表反转
students.reverse()
print(students)

list_int = [2,5,1,67,2,3,78,2,4,9]
list_int.sort()#默认是从小到大
list_int.sort(reverse=True) #加上reverse=True就可以从大到小
print(list_int)

# 说出全班学员的姓名
# 当你只是使用列表数据时，不需要用索引
for name in students:
    print(f'欢迎:{name}')

# 当你想根据索引去操作列表中的数据时
# 给所有学员的姓名后都追加_码同学
for i in range(len(students)):
    # print(students[i])
    students[i] = students[i]+'_码同学'
print(students)

# 统计全班姓王的同学个数
# ['王五', '王五', '李思思', '张三']
students = ['王五', '王五', '李思思', '张三']
count = 0
for name in students:
    if name.startswith('王'):
        count += 1
print(f'姓王的同学总共有{count}')
# print(id(students))

# 对于列表来说，存储的数据类型是啥都可以的
list1 = [1,13.5,True,'shh']
# 将list1合并到students上
students.extend(list1) #会将括号里的对象拆成一个个的数据，依次追加到原列表上
# students.append(list1) #append会将括号里的对象当做一个数据，追加到原列表上
print(students)
# 列表嵌套
"""
三组学员
'张三','李四','王五'
'张三三','李四四','王五五'
'张三三三','李四四四','王五五五','赵六'
"""
students1 = ['张三','李四','王五']
students2 = ['张三三','李四四','王五五']
students3 = ['张三三三','李四四四','王五五五','赵六']
students = [students1,students2,students3]
print(students)
for students_array in students:
    for name in students_array:
        print(name)
# 我想知道第二组第二个学员姓名是啥
print(students[1][1])
# print(students+list1)


# 列表推导式，尽量少用，因为不好理解
# 列表适用于比较简单的逻辑
list2 = [1,6,3,7,8,13,20]
# 我想得到这个list2中数据为偶数的所有数据组成的列表
# 使用普通方式得到
list3 = []
for i in list2:
    if i % 2 == 0:
        list3.append(i)
print(list3)
# 使用列表推导式得到
list4 = [value for value in list2 if value % 2 == 0]
print(list4)

students = ['王五', '王五', '李思思', '张三']
# 使用列表推导式，得到students，以王开头的数据
list5 = [name for name in students if name.startswith('王')]
print(list5)

# 面试题：l= ['Hello', 'World', 18, 'Apple', None],
# 对l列表进行操作，把每个字符串变成小写字母，数字和None保持原样，然后重新返回一个新列表
l= ['Hello', 'World', 18, 'Apple', None]
l1 = []
for i in l:
    if isinstance(i,str):
        i = i.lower()
    l1.append(i)
print(l1)

