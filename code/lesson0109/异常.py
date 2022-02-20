# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/1/16  4:08 下午
# s=[1,2,3,4]
#
# try:
#     a = 2 / 1
#     print(a)
#     print(s[1])
#     print('打印完成')
# except Exception as e:
#     print(f'列表打印失败,失败原因：{e}')
# # except ZeroDivisionError as z:
# #     print(z)
# else:
#     print('代码未报错，就执行这里的语句')
# print('代码可继续执行')

'''异常抛出'''
def add(a,b):
    if isinstance(a,int) and isinstance(b,int):
        sum=a+b
    else:
        raise  Exception('数据类型必须是int')
    return sum
def manager():
    try:
        add(2, 'ssh')
    except Exception as e:
        print(f'我也处理不了，需向上级反馈\n{e}')
        raise Exception
if __name__=='__main__':
    # add(2,'ssh')
    manager()
    print('继续啊')