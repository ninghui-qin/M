# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-01-23 16:16
# @Copyright：北京码同学
from lesson0123.stu_operate import StuOperate
from lesson0123.student import Student


class Manager:

    @classmethod
    def welcome(cls):
        print('==========欢迎登录学员管理系统==========')
        # print('请输入你的操作：新增(1),查询(2),删除(3),修改(4),退出(5)')

    @classmethod
    def operate(cls):
        try:
            op = int(input('请输入你的操作：新增(1),查询(2),删除(3),修改(4),退出(5)'))
        except:
            # print('输入有误，请输入你的操作：新增(1),查询(2),删除(3),修改(4),退出(5)')
            return #如果输入异常结束函数函数执行
        if op == 1:
            # 表示要新增学员
            id = input('请输入学员id:')
            name = input('请输入学员姓名:')
            phone = input('请输入学员手机号:')
            stu = Student(id,name,phone)
            print(StuOperate.add_stu(stu))
        elif op == 2:
            id = input('请输入要查询的学员id:')
            print(StuOperate.select_stu(id))
        elif op == 3:
            id = input('请输入要删除的学员id:')
            print(StuOperate.delete_stu(id))
        elif op == 4:
            id = input('请输入要修改的学员id:')
            # 要求控制台输入要修改的信息时，传入字典形式的字符串{'name':'张三','phone'='63267366'}
            attr_value_dict = input('请输入要修改的信息:')
            attr_value_dict = eval(attr_value_dict) #可以把字符串形式的字典转成真正的字典
            print(StuOperate.change_stu(id, **attr_value_dict))
        elif op == 5:
            return '退出'
    @classmethod
    def run(cls):
        cls.welcome()
        while True:
            flag = cls.operate()
            if flag == '退出':
                print('退出成功')
                break
if __name__ == '__main__':
    Manager.run()
