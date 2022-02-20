# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-01-23 11:53
# @Copyright：北京码同学


# 继承是为了代码的复用，减少冗余的重复的代码
# 所有类其实都有父类，不写的默认是object

class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):#父类中定义了方法，子类中直接继承
        print(f'{self.name} 在吃东西')

class JiQiCat(Cat):

    def __init__(self,name,age):
        super().__init__(name,age) # 为了继承父类的属性及方法，引用父类初始化方法
    # def eat(self):
    #     print(f'{self.name} 在吃东西')

    # def __init__(self,name,age):
    #     self.name = name
    #     self.age = age
class KafeiCat(Cat):
    # 在父类基础上可以扩展自己的属性，比如这个color是父类没有的
    def __init__(self,name,age,color):
        super().__init__(name, age)
        self.color = color
    # def __init__(self,name,age):
    #     self.name = name
    #     self.age = age

    # 多态 意思相同的事物的不同形态
    # 子类和父类方法名称相同，这就是多态的一种表现
    # 子类对象在调用时就会调用自己的
    def eat(self):
        print(f'{self.name} 爱喝 咖啡')
class KittyCat(Cat):
    def __init__(self,name,age):
        super().__init__(name,age)
    # def __init__(self,name,age):
    #     self.name = name
    #     self.age = age
    # def eat(self):
    #     print(f'{self.name} 在吃东西')
if __name__ == '__main__':
    jiqimao = JiQiCat('机器猫',3)
    print(jiqimao.name)
    print(jiqimao.age)
    jiqimao.eat()
    kafeicat = KafeiCat('咖啡猫',2,'白色')
    print(kafeicat.name)
    kafeicat.eat()