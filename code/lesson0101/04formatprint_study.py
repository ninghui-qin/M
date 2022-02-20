# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2021-12-26 13:40
# @Copyright：北京码同学

# 格式化输出

print('兹证明 沙陌 自 2019 年 11 月 2 日入职，在我公司担任 测试 部门 测试工程师 岗位')
# 兹证明 xxx 自 xx 年 xx 月 xx 日入职，在我公司担任 xx 部门 xxxxxxx 岗位
# 我想按照模板，只填充动态变化的数据，就可以输出相应对象
name = "沙陌"
start_year = 2017
start_month = '08'
start_day = 3
department_name = '研发中心'
job = '测试经理'
# name = '北河'
# 将上述的这些变量套在模板中对应的位置上，这个过程就可以理解成是格式化输出
# 最前面的f就可以理解成format，格式化的意思
print(f'兹证明 {name} 自 {start_year} 年 {start_month} 月 {start_day} 日入职，在我公司担任 {department_name} 部门 {job} 岗位')

print('兹证明 {} 自 {} 年 {} 月 {} 日入职，在我公司担任 {} 部门 {} 岗位'.format(name,start_year,start_month,start_day,department_name,job))

# 对于print函数来说，默认情况下每次都会换行
# 如果在输出时不想换行，可以指定print的结束符号
print('这是个不换行的语句',end='***')
print('前面这句话没换行，所以我们挨着了')
