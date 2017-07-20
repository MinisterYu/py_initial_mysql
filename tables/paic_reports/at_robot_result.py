#coding:utf-8
from database import DB

class at_robot_result():
    def __init__(self):
        self.record = DB('paic_reports','at_robot_result')

    def select_by(self,**where):
        return [ at_robot_result_Records(row) for row in self.record.select('id','project','token','plan_on','puid','status','test_host','test_suite','test_result','start_time','end_time','execution_time','include_tag','exclude_tag','passed','failed','total','pass_rate','report_link','created_by','created_date','updated_by','updated_date').where(**where).submit() ]

class at_robot_result_Records():
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
    def plan_on(self):
        return self.row[3]

    @property
    def puid(self):
        return self.row[4]

    @property
    def status(self):
        return self.row[5]

    @property
    def test_host(self):
        return self.row[6]

    @property
    def test_suite(self):
        return self.row[7]

    @property
    def test_result(self):
        return self.row[8]

    @property
    def start_time(self):
        return self.row[9]

    @property
    def end_time(self):
        return self.row[10]

    @property
    def execution_time(self):
        return self.row[11]

    @property
    def include_tag(self):
        return self.row[12]

    @property
    def exclude_tag(self):
        return self.row[13]

    @property
    def passed(self):
        return self.row[14]

    @property
    def failed(self):
        return self.row[15]

    @property
    def total(self):
        return self.row[16]

    @property
    def pass_rate(self):
        return self.row[17]

    @property
    def report_link(self):
        return self.row[18]

    @property
    def created_by(self):
        return self.row[19]

    @property
    def created_date(self):
        return self.row[20]

    @property
    def updated_by(self):
        return self.row[21]

    @property
    def updated_date(self):
        return self.row[22]
