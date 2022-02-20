# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-01-16 11:16
# @Copyright：北京码同学

# 定义一个函数，给一个任意的字符串，找到这个字符串中最后一个只出现一次的字符，并得到他的下标
# 给该函数增加返回值，让她返回找到的字符
def find_only_one(s):
    # s = 'hjhdfsrfouyyee1df'
    for c in s[::-1]:
        if s.count(c) == 1:
            index = s.index(c)
            return c # return语句会结束当前函数执行，也就是说他之后代码不会被执行
            # print语句仅仅只是为了帮我们去调试代码而已，他会将信息打印在控制台上
            # print(f'最后一个只出现一次的字符是{c},他的下标是{index}')
            # break
    # 如果没有只出现一次的字符，那么返回空字符串
    return ''
# 问题：定义函数时，什么情况下要加return，什么情况下不加
# 如果你的函数在执行完成之后要将结果提供给他人使用，那么就需要return
# 如果你的函数在执行完成之后不需要将结果提供给他人，那么就不需要return

# 多个数据返回，返回找到的字符和他的下标
def find_only_one1(s):
    """
    找到给定字符串中只出现一次的字符和他的下标
    :param s: 字符串
    :return: 返回字符和他的下标，如果没有只出现一次的数据，返回空字符串
    """
    # s = 'hjhdfsrfouyyee1df'
    for c in s[::-1]:
        if s.count(c) == 1:
            index = s.index(c)
            return c,index # return语句返回多个值时，数据类型是元组
            # print语句仅仅只是为了帮我们去调试代码而已，他会将信息打印在控制台上
            # print(f'最后一个只出现一次的字符是{c},他的下标是{index}')
            # break
    # 如果没有只出现一次的字符，那么返回空字符串
    return ''

def return_list(list1,list2):
    return list1,list2

if __name__ == '__main__':
    # 给两个任意的字符串，分别找到这两个字符串中只出现一次的字符，并将他们组合成新的字符串
    first = find_only_one('hhddkkll') #定义一个变量first来接收函数执行完成之后的返回值
    print(first)
    second = find_only_one('tyeyrrqggsgdue') #定义一个变量second来接收函数执行完成之后的返回值
    print(first+second)

    s,i = find_only_one1('tyeyrrqggsgdue') # ('u',12)
    print(s)
    print(i)
    list1,list2 = return_list([1,3,5],[2,4,6])
    print(list1)
    print(list2)
    s = 'hshshs'
    s.lower()
    s = [1,2,4]
    s.append(5)
