# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-01-16 13:30
# @Copyright：北京码同学

# 函数参数相关

# 位置参数
def user_info(name,age,gender):
    print(f'你的名字是{name},年龄{age},性别是{gender}')

# course 是一个有默认值的参数
# 作用是如果你是python自动化学员，那么在调用时，这个参数不传
# 如果你不是，那么这个参数就要传
# 注意点，定义时有默认值的参数必须在所有参数之后
def user_info1(name,age,gender='男',course='python自动化'):
    print(f'你的名字是{name},年龄{age},性别是{gender},课堂是{course}')


# 可变参数,按照位置顺序传递
# 定义时，不确定这个函数到底需要多少个参数，这个时候就可以使用可变参数
# 计算任意个数字的和
def add(*args):
    print(args)
    # print(args[1])
    sum = 0
    for i in args:
        sum += i
    print(sum)
# 可变参数，关键字参数传递方式
def user_info2(**kwargs):
    print(kwargs)

# 组合使用
def user_info3(name,*args,**kwargs):
    print(name)
    print(args)
    print(kwargs)
if __name__ == '__main__':
    # 按照定义时参数的位置顺序进行传参
    user_info('张三',18,'男')
    # 如果说一个函数的参数很多，我们可能很难记住他们的顺序
    # 可以使用关键字参数传递方式
    user_info(age=18,gender='男',name='张三')

    # 位置参数传递方式和关键字参数传递方式混合使用
    # 位置参数必须在关键字参数之前
    user_info('张三',age=18,gender='男')

    user_info1('张三',age=18,gender='男')
    user_info1('李四', age=18, gender='男',course='性能测试')

    add(2,4,6,4,6,3,2,4,5,5)
    # add()

    user_info2(name='沙陌',age=18,job='tester',laojia='陕西咸阳')
    user_info3('沙陌',18,'tester',laojia = '陕西咸阳')
    # user_info3('沙陌', 18,laojia='陕西咸阳', 'tester') #这是错误的

