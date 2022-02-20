# count = 0
# while count<1:
#     print(f'这是我第{count}次道歉')
#     count += 1
#
# # 计算1-100的所有偶数和
# i = 0
# sum =0
# while i<=100:
#     if i%2 == 0:
#         sum += i
#     print(f'当前i={i},合为{sum}')
#     i +=1


# # 计算1-100的所有偶数的和，除了88
# i = 0
# sum =0
# while i<=100:
#     if i == 88:
#         i +=1
#         continue   #continue 表示跳过本次循环，继续下一次循环。注意！！！是跳出本次循环！！！循环！！！！
#     if i%2 == 0:
#         sum += i
#     print(f'当前i={i},合为{sum}')
#     i +=1
# print(f'答案为{sum}')

# 吃3个苹果，第二个有虫子不吃
i=1
while i<=3:
    if i==2:
        print(f'吃第{i}个苹果了')