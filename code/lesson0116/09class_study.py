# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-01-16 16:57
# @Copyright：北京码同学

# plane = '飞机A'
# plane1 = '飞机B'
# plane_width = '30m'
# plane1_width = '40m'
# 描述生活的具体事物的时候，可以使用面向对象的方式

# 类，将生活某一类事物的公共属性和行为进行抽象，形成模板
# 定义
class Plane:
    # 这是飞机的模板，可以理解成图纸

    # 对于每架分机都有长、宽、高
    # __init__函数是用来做实例化时初始化信息的，对于与生俱来就必须具备的属性都在这里进行定义
    # 该函数在实例化对象时，会被默认调用
    # __init__并不是必须写的，没写的时候会有一个默认的空的__init__函数，是否需要写取决于业务
    # self指的是对象自身
    def __init__(self,name,length,width,height):
        self.name = name
        self.length = length
        self.width = width
        self.height = height
    # 飞机都能飞，飞的这个动作或者行为，在面向对象中使用函数来表示，在面向对象中函数可以叫做方法
    def fly(self):
        print(f'{self.name} 我能飞')

if __name__ == '__main__':
    a_plane = Plane(name='波音A',length=80,width=30,height=30) #通过类(模板)，去造飞机，这个过程叫做实例化对象，a_plane是Plane的一个对象
    print(a_plane.length)
    print(a_plane.width)
    print(a_plane.height)
    a_plane.fly()
    b_plane = Plane(name='波音B',length=85,width=35,height=35) #通过类(模板)，去造飞机，这个过程叫做实例化对象，b_plane是Plane的一个对象
    print(b_plane.length)
    print(b_plane.width)
    print(b_plane.height)
    b_plane.fly()

    """
    作业：
    1.需要你写一个函数，这个函数有一个string类型的入参，
        这个函数所做的事情，就是找出入参当中所有包含的子串
        （例如：abcdcccabcc是入参，bcd、bc都是子串，ac不是，包含关系，最少2个字符），
        并统计每一种子串在入参当中出现的次数，降序输出，例如ab出现了2次。
    2.给定两个字符串，取出最长公共子串
        举例：abcdefg,hakdhecdefabc,最长公共子串是cdef
    3.编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀,返回空字符串
        例如:
        输入:["flower" ,"flow" ,"flowht","flowxxx"],输出: "flow"
        输入:["dog","racecar","car"]输出:""
        解释:输入列表不存在公共前缀，返回""
    """