#coding:utf-8
from database import DB

class ucp_flag():
    def __init__(self):
        self.record = DB('paic_reports','ucp_flag')

    def select_by(self,**where):
        return [ ucp_flag_Records(row) for row in self.record.select('req_flag_id','req_flag_date','req_lockdown','created_date','created_by').where(**where).submit() ]

class ucp_flag_Records():
    def __init__(self,row):
        self.row = row

    @property
    def req_flag_id(self):
        return self.row[0]

    @property
    def req_flag_date(self):
        return self.row[1]

    @property
    def req_lockdown(self):
        return self.row[2]

    @property
    def created_date(self):
        return self.row[3]

    @property
    def created_by(self):
        return self.row[4]
