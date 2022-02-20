# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-01-16 16:07
# @Copyright：北京码同学

# 异常处理
# s = [2,3,5]
# print(s[5]) #列表总长度才是3，但是你要的是第6个索引是5，所以报错了，后续代码不会被执行
# print('列表打印完成')
# 代码报错通常会影响我们的代码执行，终端后后续代码不会被执行
# 那么有可能在你的业务上，即便报错了他也要继续执行，此时如何处理？
# 异常处理方式
# try:
#     # 这里来放有可能会出错的代码
#     s = [2, 3, 5]
#     # print(s[5]) # 索引越界的异常
#     a = 2/0
# except IndexError as e:
#     # 出错以后我要干什么
#     print(e)
#     print('虽然索引越界了，但是被我捕获了，代码继续向下走')
# except ZeroDivisionError as e:
#     print(e)
#     print('分母不能为0被我捕获到了，代码继续往下走')
# print('列表打印完成')

# 当我不知道具体会报什么错时，可以使用异常的基类来代表，基类可以代表所有异常
# try:
#     # 这里来放有可能会出错的代码
#     s = [2, 3, 5]
#     print(s[5]) # 索引越界的异常
#     a = 2 / 0
# except Exception as e:
#     print(e)
#     print('我不管你是什么异常，都会被捕获到，代表继续向下走')
# print('执行完成')

# else表示代码执行时没有异常，要执行的代码
try:
    # 这里来放有可能会出错的代码
    s = [2, 3, 5]
    print(s[5])
except Exception as e:
    print(e)
    print('我不管你是什么异常，都会被捕获到，代表继续向下走')
else:
    print('try里的代码没有报错，我就会被执行')
print('执行完成')

# finally 不管代码执行是否正常，我都会被执行
try:
    # 这里来放有可能会出错的代码
    s = [2, 3, 5]
    # print(s[5])
except Exception as e:
    print(e)
    print('我不管你是什么异常，都会被捕获到，代表继续向下走')
finally:
    print('不管代码执行是否正常，我都会被执行')
print('执行完成')

# 异常抛出
# 当你的函数不想或者没有能力处理代码异常时，可以向外抛出异常，让调用方去决定是否处理
def add(a,b):
    if isinstance(a,int) and isinstance(b,int):
        sum = a+b
    else:
        raise Exception('数据类型必须是int') #将异常信息抛出
    return sum
def manager():
    try:
        add(2,'sss')
    except Exception as e:
        # print('我能控制，那这个风险到我这里我就处理了')
        print('我也处理不了，需要向上级反馈')
        raise e
if __name__ == '__main__':
    try:
        add(2,'sss')
    except Exception as e:
        print('数据类型不一致')
    print('执行完成')