#coding:utf-8
from database import DB

class wizard_plans():
    def __init__(self):
        self.record = DB('paic_reports','wizard_plans')

    def select_by(self,**where):
        return [ wizard_plans_Records(row) for row in self.record.select('unid','project_id','plan_id','plan_date','created_date','updated_date').where(**where).submit() ]

class wizard_plans_Records():
    def __init__(self,row):
        self.row = row

    @property
    def unid(self):
        return self.row[0]

    @property
    def project_id(self):
        return self.row[1]

    @property
    def plan_id(self):
        return self.row[2]

    @property
    def plan_date(self):
        return self.row[3]

    @property
    def created_date(self):
        return self.row[4]

    @property
    def updated_date(self):
        return self.row[5]
