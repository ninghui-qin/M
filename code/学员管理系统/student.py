# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/1/23  2:36 下午
class Student:
    def __init__(self,id ,name,phone):
        self.id=id
        self.name=name
        self.phone=phone
        self.wx=''
        self.qq=''
        self.score=0

    def __str__(self):
        return f'{self.id},{self.name},{self.phone},{self.wx},{self.qq},{self.score},'

    def getname(self):
        return self.name
    def __set_name__(self,name):
        self.name=name

    def getphone(self):
        return self.name
    def __set_name__(self,phone):
        self.name=phone

    def getwx(self):
        return self.name
    def __set_name__(self,wx):
        self.name=wx

    def getqq(self):
        return self.qq
    def __set_name__(self,qq):
        self.name=qq

    def getscore(self):
        return self.score
    def __set_name__(self,score):
        self.name=score





if __name__== '__main__':
    stu1=Student(1,'张三','111')
    print(stu1)