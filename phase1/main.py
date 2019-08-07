# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   玩转彩票系统
# ------------------------(max to 80 columns)-----------------------------------


from pack_mini_loto.class_db import MiniLotoDB
import pack_mini_loto.global_var as GLV
import sys

sys.path.append('..')

# 初始化 - 连接DB
db = MiniLotoDB()

# Step2 建立彩票表
sql = 'CREATE TABLE IF NOT EXISTS mini_loto( \
    id INT UNSIGNED AUTO_INCREMENT, \
    num1 INTEGER, \
    num2 INTEGER, \
    num3 INTEGER, \
    PRIMARY KEY(id) \
)'
db.cursor.execute(sql)
db.commit()

# Step3 清空彩票数据
sql = 'DELETE FROM mini_loto'
db.cursor.execute(sql)
db.commit()

# Step4 插入所有彩票数据
print('\n----- 批量添加彩票 -----')
sql = "INSERT INTO mini_loto (num1, num2, num3) VALUES (%s, %s, %s)"
'''
val = [
    (1,2,3),
    (2,3,4),
    (3,4,5),
]
'''
tup = ()
val = []
for i in range(1, GLV.MAX_NUM + 1):
    for j in range(1, i + 1):
        for k in range(1, j + 1):
            tup = (i, j, k)
            val.append(tup)
print(val)

db.cursor.executemany(sql, val)
db.commit()
