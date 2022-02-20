# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-01-23 9:32
# @Copyright：北京码同学

"""
作业：
1.需要你写一个函数，这个函数有一个string类型的入参，
    这个函数所做的事情，就是找出入参当中所有包含的子串
    （例如：abcdcccabcc是入参，bcd、bc都是子串，ac不是，包含关系，最少2个字符），
    并统计每一种子串在入参当中出现的次数，降序输出，例如ab出现了2次。
2.给定两个字符串，取出最长公共子串
    举例：abcdefg,hakdhecdefabc,最长公共子串是cdef
3.编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀,返回空字符串
    例如:
    输入:["flower" ,"flow" ,"flowht","flowxxx"],输出: "flow"
    输入:["dog","racecar","car"]输出:""
    解释:输入列表不存在公共前缀，返回""
"""

"""
1.需要你写一个函数，这个函数有一个string类型的入参，
    这个函数所做的事情，就是找出入参当中所有包含的子串
    （例如：abcdcccabcc是入参，bcd、bc都是子串，ac不是，包含关系，最少2个字符），
    并统计每一种子串在入参当中出现的次数，降序输出，例如ab出现了2次。
分析：
手动查找子串的顺序是从第一个字符开始，往后逐步切片可以得到s[0:结束索引]
手动找子串:ab      abc abcd   abcdc abcdcc abcdccc abcdccca abcdcccab abcdcccabc abcdcccabcc
         [0:2] [0:3] [0:4]  [0:5]                                              [0:最长]
         bc     bcd   bcdc   bcdcc bcdccc bcdccca bcdcccab bcdcccabc bcdcccabcc  
         [1:3] [1:4]  [1:5]  [1:6]                                    [1:最长]
         cd     cdc   cdcc   cdccc cdccca cdcccab cdcccabc cdcccabcc 
         [2:4] [2:5]  [2:6]  [2:7]                         [2:最长]
         dc     dcc   dccc   dccca dcccab dcccabc dcccabcc
         [3:5] [3:6]  [3:7]  [3:8]                [3:最长]
上述切片索引，每行数据对应的起始索引都是相同的，因此需要产生多行数据的连续性索引时可以采用循环
每行数据的结束索引都是在不断变化的，所以还需要一次循环来产生这些结束索引

统计每个子串出现的次数{'ab':1,'abc':2,'abcd':1}
有这种映射关系的，可以使用字典进行存储，将子串作为key，次数作为value

按照次数降序输出，针对字典排序，使用sorted
"""
def find_sub(s):
    sub_dict = {} # 用来存储子串及次数的字典
    for i in range(len(s)):#这个循环是用来产生每行数据的起始索引的
        for j in range(i+2,len(s)+1): #这个循环用来产生每行数据的结束索引的
            # print(s[i:j])
            sub = s[i:j]
            if sub in sub_dict:#如果子串已经存在与字典中，那么在原来的次数基础上加1
                sub_dict[sub] = sub_dict[sub]+1
            else:#如果子串没有出现过，那么就给他的次数赋值1
                sub_dict[sub]=1
    # print(sub_dict)
    # 排序
    print(sorted(sub_dict.items(), key=lambda item: item[1], reverse=True))

"""
2.给定两个字符串，取出最长公共子串
    举例：abcdefg,hakdhecdefabc,最长公共子串是cdef
# 分别找出两个字符串的所有子串，然后进行对比，找到相同的并且长度最大的
分析：
1.可以以任意一个字符串的子串作为对比目标，将他们存入到列表['a','ab','abc','abcd','abcde','abcdef','abcdefg']
2.针对子串形成的列表，按照子串长度进行排序，降序，['abcdefg','abcdef','abcde','abcd','abc']
3.遍历子串列表，判断子串列表中的元素是否出现在另个字符串中，如果存在则停止遍历，如果不存在继续遍历
"""
def find_max_sub(s1,s2):
    sub_list = []
    for i in range(len(s1)):  # 这个循环是用来产生每行数据的起始索引的
        for j in range(i + 1, len(s1) + 1):  # 这个循环用来产生每行数据的结束索引的
            sub = s1[i:j]
            sub_list.append(sub)
    # 针对子串列表按照子串长度进行排序
    sub_list.sort(key=len,reverse=True)
    #['abcdefg','abcdef','abcde','abcd','abc']
    # 遍历子串列表，判断子串列表中的元素是否出现在另个字符串中
    for sub in sub_list:
        if sub in s2:
            return sub
    return ''#没有公共子串时返回空字符串

"""
3.编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀,返回空字符串
    例如:
    输入:["flower" ,"flow" ,"flowht","flowxxx"],输出: "flow"
    输入:["dog","racecar","car"]输出:""
    解释:输入列表不存在公共前缀，返回""
分析：
以任意一个元素作为子串获取目标，然后遍历列表其他元素分别判断是否是前缀即可
1.只需要得到某个字符串元素，从第一个字符开始的所有子串
2.最长的公共前缀，所以最好是截取子串时，倒着来
  flower、flowe、flow、flo、fl、f
3.使用子串去判断是否是给定列表中其他的元素的前缀，如果都是，说明找到了，有任何一个不是，就继续循环
"""
def find_max_prefix(list1:list): #list1:list表示声明参数list1是list类型的对象
    str1 = list1[0] #以任意一个去找子串
    sub_list = []
    for i in range(1,len(str1)+1):
        # print(str1[0:i])
        sub_list.append(str1[0:i])
    sub_list.reverse() #列表反转 ['flower', 'flowe', 'flow', 'flo', 'fl', 'f']
    # print(sub_list)
    for prefix in sub_list:
        flag = False #这表示prefix是否斗都是列表中其他元素的前缀
        for str in list1:
            if str.startswith(prefix):
                flag = True
            else:
                flag = False
                break
        if flag:
            return prefix
    return '' #如果上面的循环没有走到return prefix，那么就会返回空字符串
if __name__ == '__main__':
    # find_sub('abcdcccabcc')
    # print(find_max_sub('abcdefg', 'hakdhecdefabc'))
    print(find_max_prefix(["dog","racecar","car"]))

