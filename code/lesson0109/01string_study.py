# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-01-09 10:21
# @Copyright：北京码同学

# 字符串拼接
agreement = 'http://'
ip = '192.168.1.1'
url = '/mtx'
# 将上面三个字符串变量进行拼接
api_url = agreement + ip + url
print(api_url)
api_url = f'这是拼接出的url地址:{agreement}{ip}{url}'
print(api_url)

name = 'shamo'
# 通过下标得到某个字符时，使用变量名称[index]
print(f'第三个字符是{name[2]}')

# 我要得到前3个字符
# 可以使用切片来得到某一段的内容
# 切片的意思可以这样理解，相当于给你一把剪刀，从开始位置剪断，再从结束位置剪断，最终留下来的就是你要的
# [:3] 冒号前面指的是开始位置索引，不写的话默认是0，冒号后面指的是结束位置的索引，结果中不包含结束索引对应的值
print(f'前三个字符是:{name[:3]}')
# 我要得到name中的ham
print(name[1:4])
# 我要得到hamo,如果结束位置是最后，那么冒号后边不写东西
print(name[1:])
s = 'ghdkfhagfsfjdkkffhhd'
# 我要得到s这个字符串中，所有的奇数位置对应的字符,gdfaffdkfh
# [::2] 第一个冒号前后都没有，说明起始和开始是整个字符串
#  第二个冒号后面跟的是步长，指的是切片时的间隔
# 如果不写步长，默认是1
print(s[::2])

s = '沙陌是老师'
# 我想将s反向输出 师老是陌沙
# 步长不仅仅是切片时的间隔，还可以根据正负数来指定切片的方向，正数就是从前到后，负数就是从后到前
print(s[::-1])

# 反向索引
# 我想得到老师这两字
print(s[-2:])

print(s[3:-1:-1])
print('xxxx{}'.format(s[-2:3:-1]))

filepath = 'c:/abc/dd/hhsh.xlsx'
# 通过文件路径得到文件的后缀
print(filepath[-4:])


# 遍历字符串
s = 'shamo is teacher'
# 将s里的字符都单独输出
# print(s[0])
# print(s[1])
# print(s[2])
# for i in s:
#     print(i)
# 我想知道s里is出现的位置
start_index = s.find('is') #这个函数得到的是is这个字符串出现在s字符串中的起始位置
print(start_index)
# 我想知道isa是否出现在s里，find后返回结果是-1，则说明不存在
start_index = s.find('isa')
print(start_index)

s = 'shamo is the best teahcer,shamo is python auto'
# 我想将s里的shamo换成北河
s1 = s.replace('shamo','北河') #replace不会修改原有字符串，而是生成了一个新的字符串,默认情况下会替换所有的目标字符串
print(s1)
# 替换次数
s2 = s.replace('shamo','北河',1)
print(s2)
s = 'shamo is the best teahcer'
# 我要得到s里所有的单词
#默认是以空格进行分割，分割后的结果是一个列表，原字符串没有变化，新生成一个列表
print(s.split())

s = '1080*1920'
print(s.split('*'))
s = '大学，高中，初中，小学'
print(s.split('，'))
s.split('，',1) #这个数字表示分割的次数 ['大学', '高中，初中，小学']
print(s.split('，', 2)) # ['大学', '高中', '初中，小学']


# 大小写转换
s = 'hEllo'
print(s.lower()) #转成小写，不会改变原字符串，而是新生成一个
print(s.upper()) #转成大写，不会改变原字符串，而是新生成一个
# 传入一个方向，判断是上下左右
# direction = input('请输入up/down/left/right:')
# if direction.lower() == 'up':
#     print('上')
# elif direction.lower() == 'down':
#     print('下')

# 去掉两端的空格
s = '   码同学 '
print(s)
print(s.lstrip()) #去掉左边空格
print(s.rstrip()) #去掉右边空格
print(s.strip()) #去掉两端空格
# 如果字符串中间有空格
s = '码 同   学'
print(s.replace(' ', ''))

s = '沙陌'
# 判断某个人是否姓什么？
print(s.startswith('沙'))#True startswith判断某个字符串是否以xx开头
s = '上官婉儿'
print(s.startswith('上官'))

filepath = 'c:/abc/dd/hhsh.xlsx'
print(filepath.endswith('xlsx')) #判断字符串是否以xxx结尾

s = 'hsh*'
# 判断是否是一个纯字母字符串
print(s.isalpha())
# 判断一个字符串是否是纯数字
s = '76336'
print(s.isdigit())

s = 'shamo is teacher'
print(s[::-1])

# 有数字123，将其反转成321，注意如果是负数-123，反转后是-321
a = -435366
if a>0:
    a = str(a) #将数字转换成字符串
    print(a[::-1])
else:
    a = str(a)  # 将数字转换成字符串
    # print(a) #-123
    # print(a[1:])
    # print(a[1:][::-1])
    a = a[0]+a[1:][::-1]
    print(a)

s = 'hhshk fhhdh  ashg  fjkdhfh  sdjhhh asggd  fjj'
# 字符串长度
print(len(s))


