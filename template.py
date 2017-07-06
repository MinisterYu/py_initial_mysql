#! /usr/bin/env python
#coding:utf-8

table_class='''#coding:utf-8
from database import DB

class {1}():
    def __init__(self):
        self.record = DB('{0}','{1}')

    def select_by(self,**where):
        return [ {1}_Records(row) for row in self.record.select({2}).where(**where).submit() ]
'''

records_class='''
class {0}_Records():
    def __init__(self,row):
        self.row = row
'''

records_info='''
    @property
    def {0}(self):
        return self.row[{1}]
'''

