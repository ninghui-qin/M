# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-01-16 14:17
# @Copyright：北京码同学

# 匿名函数
# 如果一个函数有一个返回值，并且只有一句代码，并且这个函数只是用一次，可以使用lambda简化
def fn1():
    return 200
fn2 = lambda: 200

def add(a,b):
    return a+b
# lambda 冒号之前写的匿名函数的入参定义，冒号之后写的匿名函数的返回值
add1 = lambda a,b:a+b

# 我有一个字典，字典里存储的是各个学员的考试成绩，姓名:成绩
scores = {'张三':80,'李四':100,'王五':75,'赵六':78}
# 针对scores这个字典按照成绩进行排序
# 引入一个sorted函数来排序
# sorted 第一个参数是可迭代对象
# scores.items() 这表示拿到字典的键值对，每一个键值对就是一个item(张三,80) item(李四,100) item(王五,75)
def return_score(item):
    return item[1]
print(sorted(scores.items(), key=return_score))
# 上述函数return_score仅仅只用这么一次，而且只有一行代码，而且有返回值，非常符合匿名函数的场景
print(sorted(scores.items(), key=lambda item: item[1],reverse=True)) #成绩从大到小
if __name__ == '__main__':
    print(fn1())
    print(fn2())
    print(add1(2,5))