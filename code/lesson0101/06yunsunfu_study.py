# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2021-12-26 14:26
# @Copyright：北京码同学

# 运算符

# 算数运算符

print('+:{}'.format(10+20))
print('-:{}'.format(10-20))
print('*:{}'.format(10*20))
# 除法比较特殊,不管他的结果是整除，还是整除不了，结果的类型都是float
print('10除以3等于：{}'.format(10/3))
print('10除以2等于：{}'.format(10/2))
res = 10/2
print(type(res))
# 取整,指的是除了以后，不管小数是多少，直接取整数部分
print('20除以3取整等于：{}'.format(20//3))

# 取余数，20/3=6 余2
print('20除以3取余数等于：{}'.format(20%3))

# 取幂，就是几的几次方，比如2的3次方
print('2的3次方是：{}'.format(2**3))
# ()是用来控制计算表达式的计算顺序的
print('10+2*3先算加法：{}'.format((10+2)*3))

# 赋值运算符
a = 1
a=b=c = 2 # a,b,c三个变量同时赋值，都等于2
a,b,c = 3,'bb',19.3 # 三个变量按照前后对应的顺序位置进行赋值


# 复合赋值运算符
a = 1
a += 2 # 意思是在a原来的基础上增加个2，再赋值给a，相当于a = a+2
print(a) #3
b = 10
b -= 6 # 表示在b原来的基础上减去6，然后再赋值给b,相当于b = b-6
print(b) # 4
c = 2
c *= 3 # 表示在c原来的基础上乘以3，然后再赋值给c,相当于c = c*2
print(c) #6
d = 10
d /= 3 # 表示在d原来的基础上除以3，然后再赋值给d,相当于d = d/3
print(d)
e = 10
e //=3 # 表示在e原来的基础上除以3取整，然后再赋值给e,相当于e = 10//3
print(e)


# 比较运算符
print('3是否等于3：{}'.format(3==3)) #判断相等用双等号
print('3是否大于3：{}'.format(3>3))
print('3是否不等于3：{}'.format(3!=3))

# 逻辑运算符
a = 20
b = 10
c = 21
# 对于and来说，俩边的结果都是True，他的结果才是True，任何一个是False，那么结果就是False
print('a是否大于b并且大于c：{}'.format(a>b and a>c))
# 对于or来说，两边的结果都是False，他的结果才是False，任何一个是True，那么结果就是True
print('a大于b或者大于c：{}'.format(a>b or a>c)) # True or False 最终结果是True

# not表示取反，你是True，not后就变成False，你是False，not后就变成True
print(not a>b)

# 从控制台输入一个数字，打印出他是否是偶数
a = input('请输入你的数字:')
a = int(a)
# 针对数字除2，如果余数为0则说明是偶数
print(a%2==0)

a = 3.44577
print(round(a,2))
