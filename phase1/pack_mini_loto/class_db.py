# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   学习通过类来使用数据库
# ------------------------(max to 80 columns)-----------------------------------



import mysql.connector


class MiniLotoDB():

    '''
    __myconn = None
    __mycursor = None
    '''

    def __init__(self):
        self.__myconn = None
        self.__mycursor = None
        self.get_conn()
        self.get_cursor()
        return

    def get_conn(self):
        self.__myconn = mysql.connector.connect(
            host='211.167.105.132',
            database='stdt201909',
            user='student001',
            password='liangBa_2019',
            auth_plugin='mysql_native_password',
        )
        return self.__myconn

    def get_cursor(self):
        self.__mycursor = self.__myconn.cursor()
        return

    def commit(self):
        self.__myconn.commit()
        return

    @property
    def conn(self):
        return self.__myconn

    @property
    def cursor(self):
        return self.__mycursor
