# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-01-23 14:49
# @Copyright：北京码同学

# 读取和写入数据文件方法
from lesson0123.student import Student


class FileOperate:

    def __init__(self):
        self.filepath = 'students_db.txt'

    def read(self):
        """
        读取数据需要转换成{1:stu1,2:stu2,3:stu3,4:stu4} 这样的结构
        :return:
        """
        stus_dict = {} #读取转成字典，作为中间数据对象
        with open(file=self.filepath,mode='r',encoding='UTF-8') as f:
            all_lines = f.readlines() #all_lines是个列表，一个元素代表一行数据，代表一个学员
            # print(all_lines)
            for line in all_lines:
                # line 是'1,张三,18998880001,hhsg,27366,0\n'
                # 通过逗号分割，再通过索引得到学员的各项信息
                line_spit = line.split(',')
                id = line_spit[0]
                name = line_spit[1]
                phone = line_spit[2]
                wx = line_spit[3]
                qq = line_spit[4]
                score = line_spit[5][:-1] # '86\n'
                # print(score)
                stu = Student(id,name,phone) #实例化学员对象
                stu.setWx(wx)
                stu.setQQ(qq)
                stu.setScore(score)
                stus_dict[id] = stu
        return stus_dict

    def write(self,stus_dict:dict): #stus_dict:dict 传入的参数，冒号后边表示这个参数的类型
        # stus_dict {1:stu1,2:stu2,3:stu3,4:stu4}
        with open(file=self.filepath,mode='w',encoding='UTF-8') as f:
            # f.write('学员信息')
            # 遍历传进来的字典对象里的所有value，
            for stu in stus_dict.values():
                # 注意这里的stu是个学员对象
                f.write(str(stu)) #学员对象不是字符串类型，无法写入的，所以将其转成字符串str(stu)，会自动调用学员类中的__str__
                f.write('\n') #换行
if __name__ == '__main__':
    stus_dict = FileOperate().read()
    print(stus_dict)
    # stus_dict['1'].setName('张三三')
    # FileOperate().write(stus_dict)
