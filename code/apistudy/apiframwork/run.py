# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/3/26  9:45 下午
import os

import pytest

if __name__ == '__main__':
    #执行时，会自动识别pytest.ini里的规则
    pytest.main()

    os.system('allure generate ./report/data -o ./report/html --clean')