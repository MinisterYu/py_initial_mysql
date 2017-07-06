#coding:utf-8
from database_set import DB

class reports():
    def __init__(self):
        self.record = DB()

    def select_by(self,**where):
        return [ reportsRecords(row) for row in self.record.select('project','version','lamp','fixed').where(**where).submit() ]

class reportsRecords():
    def __init__(self,row):
        self.row = row

    @property
    def project(self):
        return self.row[0]

    @property
    def version(self):
        return self.row[1]

    @property
    def lamp(self):
        return self.row[2]

    @property
    def fixed(self):
        return self.row[3]
