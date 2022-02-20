# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-01-23 10:57
# @Copyright：北京码同学

class Students:
    # 这是一个类属性的定义，类属性是和具体的某个对象没有关系的，但是属于这个类公共的属性信息
    # 调用时，直接使用类名称进行调用即可
    school = '码同学'

    # 类方法使用@classmethod进行装饰的方法
    # cls指的是当前类
    # 类方法是和实例没有什么关系的，属于当前类所代表的事物的公共行为
    # 调用时，使用类名.方法名
    @classmethod
    def lingjiang(cls):
        print(f'{cls.school}的所有学员都可以来领推荐奖了')
    @staticmethod
    def suibian():
        print('这是一个静态方法')
    # 定义一个初始化方法，在这里针对学员对象的初始信息进行定义和赋值
    # 在init中声明的都是实例或者对象属性
    def __init__(self,name,age,banji):
        self.name = name
        self.age = age
        self.banji = banji

    # 实例方法，是一个对象方法，方法中带着self就说明他是一个实例方法
    def sayinfo(self):
        print(Students.school) #实例方法中可以通过类名.属性名或者类名.方法名 调用类属性或者类方法
        print(f'我的名字叫{self.name},今年{self.age}岁')
    def write_homework(self):
        print(f'{self.name}正在写作业')
    # 静态方法其实和当前类或者当前类的对象没有什么关系，只所以写在类里仅仅是为了代码上的维护而已
    # 他其实就是一个写在类里的普通函数，调用时，使用类名.函数名
    @staticmethod
    def suibian():
        print('这是一个静态方法')

#
# def suibian():
#     print('这是个普通函数')



if __name__ == '__main__':
    Students.suibian()
    Students.lingjiang() #调用类方法
    zhangsan = Students(name='张三',age=18,banji='20211226') #实例化对象过程，会自动调用init初始化
    zhangsan.sayinfo() # 这是对象调用方法，
    zhangsan.write_homework()
    print(zhangsan.school)
    zhangsan.lingjiang()
    print(Students.school) #使用类名称直接调用类属性
    lisi = Students(name='李四',age=20,banji='20211226')
    lisi.sayinfo()
    lisi.write_homework()
