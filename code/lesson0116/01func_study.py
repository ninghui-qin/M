# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-01-16 10:23
# @Copyright：北京码同学

# 函数的基本定义
# func_name表示这个函数的名称，自定义的
# 函数名称后面的小括号里可以放这个函数的入参
# :号表示函数体具体代码的实现的开始
def func_name():
    print('11111')
    # pass #仅仅只是为了占位，当你没有想好这个函数具体应该怎么写时，可以先用pass占着

# 定义一个计算两个数字的和的函数
def add():
    sum = 1+10
    print(sum)

# 定义一个计算任意两个数字的和的函数
# 任意的两个数字就是这个函数的入参
def add1(a,b):
    sum = a + b
    print(sum)

# 定义一个函数，给一个任意的字符串，找到这个字符串中最后一个只出现一次的字符，并得到他的下标
def find_only_one(s):
    # s = 'hjhdfsrfouyyee1df'
    for c in s[::-1]:
        if s.count(c) == 1:
            index = s.index(c)
            print(f'最后一个只出现一次的字符是{c},他的下标是{index}')
            break

# 有一个序列： 1/1,1/2,2/3,3/5,5/8,8/13...
# 定义一个函数，计算上述序列前任意项的和
def add2(n):
    fenzi = 1
    fenmu = 1
    sum = 0  # 这是总和
    for i in range(n):
        # print(f'{fenzi}/{fenmu}')
        cur = fenzi / fenmu  # 这是数据
        sum += cur
        fenzi, fenmu = fenmu, fenzi + fenmu  # 这是python两数交换的简单写法
    print(sum)
# 定义一个函数，计算给定日期是这一年的第多少天
def jisuan_date(year,month,day):
    # year = int(input('请输入年:'))
    # month = int(input('请输入月:'))
    # day = int(input('请输入日:'))
    sum = 0  # 这个变量是用来存储总天数的，也是用来做累加计算的
    for i in range(1, month):  # range中写月份的限制，注意是没有0月的，但是range(month)是从0开始，改成range(1,month)
        # 这里的i就代表了你要计算的每一个月份
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
            sum += 31  # 等同于sum = sum+31
        elif i == 4 or i == 6 or i == 9 or i == 11:
            sum += 30
        elif i == 2:
            # 月份是2月的话，闰年是29天，平年是28天
            # 普通闰年：公历年份是4的倍数，且不是100的倍数的，为闰年（如2004年、2020年等就是闰年）。
            if year % 4 == 0 and year % 100 != 0:
                sum += 29
            # 世纪闰年：公历年份是整百数的，必须是400的倍数才是闰年（如1900年不是闰年，2000年是闰年）。
            elif year % 400 == 0:
                sum += 29
            else:
                sum += 28
    sum += day
    print(f'{year}年{month}月{day}日是{year}年的第{sum}天')
if __name__ == '__main__':
    # 这个main是为了区分当前脚本文件中的各种定义和调用调试的
    # 函数调用，函数必须被调用才会被执行
    func_name()
    add()
    add1(10,20)  #函数调用时括号中要写什么数据是根据函数的定义来的
    # add1() #这是错误的
    add1(1.3,4.56)
    add1('abc','hjk')
    find_only_one('hhdhgfdfteryytww')
    find_only_one('dhqerweffds')
    find_only_one('afrrewr')
    add2(5)
    add2(8)
    add2(999)
    jisuan_date(2012,10,23)