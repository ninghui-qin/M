# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/3/27  10:38 下午
import pandas

from setting import DIR_NAME


def read_excel(filepath,sheet_name):
    # keep_default_na 为FALSE代表当你的单元格为空时
    pandas.read_excel(DIR_NAME+filepath,sheet_name=sheet_name,keep_default_na=False,engine='openpyxl')
    
    pass