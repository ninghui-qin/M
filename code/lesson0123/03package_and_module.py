# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-01-23 13:52
# @Copyright：北京码同学

# 模块:简单理解一个模块其实就是一个python文件
# 包: 就是一个目录，包存在的意义帮我把代码分类管理(按照一定的维度)

# 如果在当前文件中要使用其他文件中的函数或者类或者变量时，需要先导入
from homework import find_sub, find_max_sub  # 从homework这个模块下导入find_sub这个函数

find_sub('shjdhhdgfggfsff')

find_max_sub('sahgdas','djhdfhhf')

from lesson0116.homework import add
add()

# 针对导入的函数或者类起一个别名
from homework import find_max_sub as fms
fms('shdhhsd','aggsffgd')

# 学员管理系统
# 学员信息包括 姓名、手机号、微信、qq、成绩
# 学员的存储，存到文件中
# 系统包括几个核心操作，学员新增、学员修改、学员删除、学员查询