# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/3/10  11:07 下午
import pymysql
import json

class DB:
    def __init__(self):
        self.db=pymysql.Connect(
            host = '121.42.15.146',
            port = 3306,
            user = 'root',
            password = 'Testfan#123',
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.DictCursor
        )


    def select(self,sql):

        cursor = self.db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        self.db.commit()
        self.db.close()
        # print(data)
        return data




if __name__ == '__main__':
    db=DB()
    db.select('select * from mtxshop_system.es_logi_company ORDER BY id desc ')