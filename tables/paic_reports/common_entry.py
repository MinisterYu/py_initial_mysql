#coding:utf-8
from database import DB

class common_entry():
    def __init__(self):
        self.record = DB('paic_reports','common_entry')

    def select_by(self,**where):
        return [ common_entry_Records(row) for row in self.record.select('entry_id','entry_code','entry_value','entry_desc','created_date','created_by','updated_date','updated_by').where(**where).submit() ]

class common_entry_Records():
    def __init__(self,row):
        self.row = row

    @property
    def entry_id(self):
        return self.row[0]

    @property
    def entry_code(self):
        return self.row[1]

    @property
    def entry_value(self):
        return self.row[2]

    @property
    def entry_desc(self):
        return self.row[3]

    @property
    def created_date(self):
        return self.row[4]

    @property
    def created_by(self):
        return self.row[5]

    @property
    def updated_date(self):
        return self.row[6]

    @property
    def updated_by(self):
        return self.row[7]
