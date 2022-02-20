# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/1/3  10:42 下午
'''
企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%；
高于100万元时，超过100万元的部分按1%提成。
从键盘输入当月利润I，求应发放奖金总数？
'''
profit=int(input('请输入当月利润(单位：万元)：'))
bonus=0
if profit >= 0 and profit <= 10:
    bonus=0.1*profit
elif profit > 10 and profit <= 20:
    bonus=1+(profit-10)*0.075
elif profit > 20 and profit <= 40:
    bonus=1+10*0.075+(profit-20)*0.05
elif profit > 40 and profit <= 60:
    bonus=1+10*0.075+20*0.05+(profit-40)*0.03
elif profit > 60 and profit <= 100:
    bonus=1+10*0.075+20*0.05+20*0.03+(profit-60)*0.015
elif profit > 100 :
    bonus=1+10*0.075+20*0.05+20*0.03+40*0.015+(profit-100)*0.01
else:
    bonus=0
print(bonus)