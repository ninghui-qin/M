# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/3/27  10:38 下午
import pandas

from setting import DIR_NAME


def read_excel(filepath,sheet_name):
    # keep_default_na 为FALSE代表当你的单元格为空时,返回的是空字符串。不设置这个参数的话返回的是NA
    #表示选择的底层的引擎是什么
    pandas.read_excel(DIR_NAME+filepath,sheet_name=sheet_name,keep_default_na=False,engine='openpyxl')
    res = pandas.read_excel(DIR_NAME+filepath,sheet_name=sheet_name,keep_default_na=False,engine='openpyxl')
    # print(res)
    # 需要将拿到的数据换成列表套列表的形式
    data=[] #总的数据存储
    line_count=res.shape[0] # 表示总行数
    cols_count=res.shape[1] # 表示总列数
    # print(line_count,cols_count)
    # print(res.shape)
    for l in range(line_count):
        lines=[]
        for c in range(cols_count):
            cell_data=res.iloc[l,c]
            lines.append(cell_data)
        data.append(lines)
    return data

if __name__ == '__main__':
    read_excel('/data/mtxshop_testdata.xlsx','添加购物车')