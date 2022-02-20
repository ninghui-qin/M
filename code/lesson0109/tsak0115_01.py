# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/1/16  5:24 下午
'''
1.需要你写一个函数，这个函数有一个string类型的入参，
    这个函数所做的事情，就是找出入参当中所有包含的子串
    例如：abcdcccabcc是入参，bcd、bc都是子串，ac不是，包含关系，最少2个字符），
    并统计每一种子串在入参当中出现的次数，降序输出，例如ab出现了2次。
2.给定两个字符串，取出最长公共子串
        举例：abcdefg,hakdhecdefabc,最长公共子串是cdef
3.编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀,返回空字符串
        例如:
        输入:["flower" ,"flow" ,"flowht","flowxxx"],输出: "flow"
        输入:["dog","racecar","car"]输出:""
        解释:输入列表不存在公共前缀，返回""
'''

list0=[]
dict1={}
dict2={}
str1 = 'abcdcccabcc'
str2='hakdhecdefabc'
def find_substr(self):
    '''找出入参当中所有包含的子串'''
    for i in range(len(self)-1):
        for j in range(i+1, len(str1)):
            substr=self[i:j+1]
            list0.append(substr)
    return list0
def substr_count(self):
    '''找出列表中的数据出现的次数并降序排出来'''
    for n in self:
        dict1[n]=self.count(n)
    # print(dict1)
    return sorted(dict1.items(),key=lambda x:x[1],reverse=True)
    # sorted(dict1.items(),cmp=lambda x,y:cmp(x[1],y[1]))
    # python3.4.3之后的版本都没有cmp函数了，所有这样用回报错'cmp' is an invalid keyword argument for sort()
def find_common_str(str1,str2):
    '''寻找公共子串，并放进列表里'''
    list1=find_substr(str1)
    list2=find_substr(str2)
    set2=set(list1)&set(list2)
    # print(f'公共子串都有：{list(set2)}')
    return list(set2)
def common_str_l(list3):
    '''找最长的公共子串,若只有一个则返回一个子串，若有多个则返回列表'''
    longest = list3[1]
    for i in range(1,len(list3)-1):
        if len(list3[i])>len(longest):
            longest=list3[i]
        elif len(list3[i])==len(longest):
            longest_list=[]
            longest_list.append(longest)
            longest_list.append(list3[i])
        if longest in longest_list:
            return longest_list
        else:
            return longest
'''
3.编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀,返回空字符串
        例如:
        输入:["flower" ,"flow" ,"flowht","flowxxx"],输出: "flow"
        输入:["dog","racecar","car"]输出:""
        解释:输入列表不存在公共前缀，返回""
'''
def common_sta_atr(list3):
    '''寻找最长公共前缀'''

    str3=list3[0]
    for i in range(len(str3),0,-1):
        substr=str3[0:i]
        for j in list3:
            if j.startswith(substr) :
                if list3.index(j)==len(list3)-1:
                    return substr
            else:
                if i==1:
                    substr=""
                    print('输入列表不存在公共前缀，',end=',')
                    return substr
                break
if __name__ =='__main__':
    list1=find_substr('abcdcccabcc')
    task1=substr_count(list1)
    print(f'第一题答案为{task1}')

    common_str=find_common_str('abcdefg', 'hakdhecdefabc')
    task2=common_str_l(common_str)
    print(f'第二题答案为{task2}')

    task3=common_sta_atr(["flow" ,"floweee" ,"flowht","flowxxx"])
    print(f'第三题答案为{task3}')
    task3_1=common_sta_atr(["dog","racecar","car"])
    print(f'第三题答案为{task3_1}')


