#coding:utf-8
from database import DB

class at_junit_result():
    def __init__(self):
        self.record = DB('paic_reports','at_junit_result')

    def select_by(self,**where):
        return [ at_junit_result_Records(row) for row in self.record.select('id','project','token','puid','host_name','host_ip','plan_on','start_time','end_time','execution_time','status','passed','failed','total','ignore','pass_rate','created_date').where(**where).submit() ]

class at_junit_result_Records():
    def __init__(self,row):
        self.row = row

    @property
    def id(self):
        return self.row[0]

    @property
    def project(self):
        return self.row[1]

    @property
    def token(self):
        return self.row[2]

    @property
    def puid(self):
        return self.row[3]

    @property
    def host_name(self):
        return self.row[4]

    @property
    def host_ip(self):
        return self.row[5]

    @property
    def plan_on(self):
        return self.row[6]

    @property
    def start_time(self):
        return self.row[7]

    @property
    def end_time(self):
        return self.row[8]

    @property
    def execution_time(self):
        return self.row[9]

    @property
    def status(self):
        return self.row[10]

    @property
    def passed(self):
        return self.row[11]

    @property
    def failed(self):
        return self.row[12]

    @property
    def total(self):
        return self.row[13]

    @property
    def ignore(self):
        return self.row[14]

    @property
    def pass_rate(self):
        return self.row[15]

    @property
    def created_date(self):
        return self.row[16]
