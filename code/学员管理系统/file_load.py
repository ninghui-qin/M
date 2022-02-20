# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/1/23  2:50 下午


class Fileoperate:

    def __init__(self):
        self.filepath='students_db.txt'

    def read(self):
        '''
        读取数据，将数据转换成这种格式：{1:stu1,2:stu2,3:stu3}
        :return:
        '''
        stus_dict={}
        with open(file=self.filepath,mode='r') as f:
            all_lines=f.readlines()   #all_lines是一个列表
            print(all_lines) # 结果为：['1,张三三,18998880001,hhsg,27366,0\n', '2,李四,18812345678,wxyhg,87472,85\n', '3,赵六,18812345679,wxyhw,87473,86']
            for student in all_lines: # student 是 '1,张三三,18998880001,hhsg,27366,0\n'
                id  = student.split(',')[0]
                name= student.split(',')[1]
                phone= student.split(',')[2]
                wx  = student.split(',')[3]
                qq  = student.split(',')[4]
                score= student.split(',')[5]
                

    # def write(self,stus_dict:dict):


if __name__ == '__main__':
    Fileoperate().read()