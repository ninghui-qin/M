# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-01-23 14:34
# @Copyright：北京码同学

# 定义学员类
class Student:

    # id,姓名、手机号、微信、qq、成绩
    def __init__(self,id,name,phone):
        self.id = id
        self.name = name
        self.phone = phone
        self.wx = ''
        self.qq = ''
        self.score = 0
    # 默认情况下我们直接使用对象时，他是对象的内存地址
    # 但是我们希望该类的对象可以转换成某种格式的字符串时，就可以使用__str__来实现
    def __str__(self):
        return f'{self.id},{self.name},{self.phone},{self.wx},{self.qq},{self.score}'
    # 自定义方法也能实现，但需要调用
    def convert_to_str(self):
        return f'{self.id},{self.name},{self.phone},{self.wx},{self.qq},{self.score}'

    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name
    def getPhone(self):
        return self.phone
    def setPhone(self,phone):
        self.phone = phone
    def getWx(self):
        return self.wx
    def setWx(self,wx):
        self.wx = wx
    def getQQ(self):
        return self.qq
    def setQQ(self,qq):
        self.qq = qq
    def getScore(self):
        return self.score
    def setScore(self,score):
        self.score = score
if __name__ == '__main__':
    stu1 = Student(1,'张三','1872636')
    # 1,张三,18998880001,hhsg,27366,0
    print(stu1)
    print(stu1.convert_to_str())
    print(stu1.getName())
    stu1.setName('李四')

