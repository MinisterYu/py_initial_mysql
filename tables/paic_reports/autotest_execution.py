#coding:utf-8
from database import DB

class autotest_execution():
    def __init__(self):
        self.record = DB('paic_reports','autotest_execution')

    def select_by(self,**where):
        return [ autotest_execution_Records(row) for row in self.record.select('id','puid','project','host','test_suite','test_include','test_exclude','start_time','end_time','spend_time','result','total_case','passed_case','failed_case','pass_rate','status','report_link','created_date','created_by','updated_date','updated_by').where(**where).submit() ]

class autotest_execution_Records():
    def __init__(self,row):
        self.row = row

    @property
    def id(self):
        return self.row[0]

    @property
    def puid(self):
        return self.row[1]

    @property
    def project(self):
        return self.row[2]

    @property
    def host(self):
        return self.row[3]

    @property
    def test_suite(self):
        return self.row[4]

    @property
    def test_include(self):
        return self.row[5]

    @property
    def test_exclude(self):
        return self.row[6]

    @property
    def start_time(self):
        return self.row[7]

    @property
    def end_time(self):
        return self.row[8]

    @property
    def spend_time(self):
        return self.row[9]

    @property
    def result(self):
        return self.row[10]

    @property
    def total_case(self):
        return self.row[11]

    @property
    def passed_case(self):
        return self.row[12]

    @property
    def failed_case(self):
        return self.row[13]

    @property
    def pass_rate(self):
        return self.row[14]

    @property
    def status(self):
        return self.row[15]

    @property
    def report_link(self):
        return self.row[16]

    @property
    def created_date(self):
        return self.row[17]

    @property
    def created_by(self):
        return self.row[18]

    @property
    def updated_date(self):
        return self.row[19]

    @property
    def updated_by(self):
        return self.row[20]
