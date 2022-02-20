# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-01-23 15:24
# @Copyright：北京码同学
from lesson0123.file_load import FileOperate
from lesson0123.student import Student


class StuOperate:

    # 在这里全部使用类属性和类方法完成
    stus_dict = FileOperate().read()

    #添加学员
    # 应该传什么参数呢，学员id？name？phone？
    # 新增学员是增加一个学员整体对象，所以我们可以传学员对象参数，而不是传某个属性
    @classmethod
    def add_stu(cls,stu:Student):#定义了一个参数stu，他的类型是Student
        # 操作都是在stus_dict上完成的
        # 如果学员id已存在不能添加
        if stu.id not in cls.stus_dict:
            cls.stus_dict[stu.id] = stu #将传进来的学员对象，加到中间数据对象字典中
            # 中间变量操作完成后将其重新写入到文件中
            FileOperate().write(cls.stus_dict)
            return '添加成功'
        else:
            return f'学员id:{stu.id}已存在，不能新增'

    # 删除学员，你得告诉我要删除谁，
    # id是可以唯一代表学员的，所以传参id
    @classmethod
    def delete_stu(cls,id):
        if id in cls.stus_dict:
            del cls.stus_dict[id]
            FileOperate().write(cls.stus_dict) #回写文件
            return '删除成功'
        else:
            return f'学员id:{id}不存在，不能删除'
    # 查询学员
    # 通过学员id查询，所以传参id
    @classmethod
    def select_stu(cls,id):
        if id in cls.stus_dict:
            stu = cls.stus_dict[id]
            return str(stu)
        else:
            return f'学员id:{id}不存在'

    # 修改学员
    # 需要告诉我你要修改谁，所以传参id
    # 你总得告诉我要修改学员的什么信息，name?phone?wx?qq?score
    # 要修改的信息不确定，并且还有一定的对象关系，name=砂沫沫，phone=162636
    @classmethod
    def change_stu(cls,id,**kwargs):
        if id in cls.stus_dict:
            stu = cls.stus_dict[id]
            # 解析传进来的kwargs,kwargs  {'name':'张三','phone'='63267366'}
            if 'name' in kwargs:
                stu.setName(kwargs['name'])
            if 'phone' in kwargs:
                stu.setPhone(kwargs['phone'])
            if 'wx' in kwargs:
                stu.setWx(kwargs['wx'])
            if 'qq' in kwargs:
                stu.setQQ(kwargs['qq'])
            if 'score' in kwargs:
                stu.setScore(kwargs['score'])
            # 修改完成之后也要回写文件
            FileOperate().write(cls.stus_dict)
            return '修改成功'
        else:
            return f'学员id:{id}不存在'


if __name__ == '__main__':
    stu = Student('4','沙陌',78326262)
    print(StuOperate.add_stu(stu))
    print(StuOperate.select_stu('3'))
    # StuOperate.change_stu('4',name='沙陌',phone='3555',qq='98877')
    # StuOperate.delete_stu('4')

    attr_value_dict = {'name':'张三','phone':'63267366','qq':'98877'}
    # print(**attr_value_dict)
    StuOperate.change_stu('4',**attr_value_dict)