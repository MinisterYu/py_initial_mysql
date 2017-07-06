#! /usr/bin/env python
#coding:utf-8

table_class='''#coding:utf-8
from database_set import DB

class {0}():
    def __init__(self):
        self.record = DB()

    def select_by(self,**where):
        return [ {0}Records(row) for row in self.record.select({1}).where(**where).submit() ]
'''

records_class='''
class {0}Records():
    def __init__(self,row):
        self.row = row
'''

records_info='''
    @property
    def {0}(self):
        return self.row[{1}]
'''

