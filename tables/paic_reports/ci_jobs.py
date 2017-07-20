#coding:utf-8
from database import DB

class ci_jobs():
    def __init__(self):
        self.record = DB('paic_reports','ci_jobs')

    def select_by(self,**where):
        return [ ci_jobs_Records(row) for row in self.record.select('id_jobs','name','related_node','method','type','cmd','manual_cases','date_created','date_updated').where(**where).submit() ]

class ci_jobs_Records():
    def __init__(self,row):
        self.row = row

    @property
    def id_jobs(self):
        return self.row[0]

    @property
    def name(self):
        return self.row[1]

    @property
    def related_node(self):
        return self.row[2]

    @property
    def method(self):
        return self.row[3]

    @property
    def type(self):
        return self.row[4]

    @property
    def cmd(self):
        return self.row[5]

    @property
    def manual_cases(self):
        return self.row[6]

    @property
    def date_created(self):
        return self.row[7]

    @property
    def date_updated(self):
        return self.row[8]
