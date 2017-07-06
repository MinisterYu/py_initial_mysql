#! /usr/bin/env python
#coding:utf-8
import pymysql

class HANDLE():

    def __init__(self,db,sql):
        self.db = db
        self.sql = sql

    def submit(self):
        rows = ()
        print 'submit sql : ',self.sql
        try:
            con = pymysql.connect(host='localhost', port=3306, user='root', passwd='',charset='UTF8')
            con.cursor()
            con.cursor().execute(self.sql)
            rows = con.cursor().fetchall()
        finally:
            con.cursor().close()
            con.close()
        return rows

class CONDITION():

    def __init__(self,db,sql):
        self.sql = sql
        self.db = db

    def where(self,**kwargs):
        if kwargs:
            condition = ' WHERE 1=1 AND '
        else:
            condition = ' WHERE 1=1 '

        _filter = ' AND '.join([ "{0}='{1}'".format( k, kwargs.get(k)) for k in kwargs ])
        sql = self.sql+condition+_filter
        # print sql
        return HANDLE(self.db,sql)

class DB():

    def __init__(self,db,table):
        self.table = table
        self.db = db

    def select(self,*rows):
        if not rows:
            raise  Exception('rows can not be null!')

        row = ','.join(rows)
        sql = 'SELECT {0} FROM {1}'.format(row,self.table)
        return CONDITION(self.db,sql)

    def update(self,**key_value):
        if not key_value:
            raise Exception('key_value can not be null!')

        row = ','.join([ "{0}='{1}'".format(k, key_value.get(k)) for k in key_value ])
        sql = 'UPDATE {1} SET {0}'.format(row,self.table)
        return CONDITION(self.db,sql)

    def insert(self,**key_value):
        if not key_value:
            raise Exception('key_value can not be null!')

        row = ','.join([ "`{0}`".format(k) for k in key_value ])
        value = ','.join([ "'{0}'".format(key_value.get(k)) for k in key_value ])
        sql = 'INSERT INTO `{2}` ({0}) VALUES ({1})'.format(row,value,self.table)
        return HANDLE(self.db,sql.format(row,value,self.table))

