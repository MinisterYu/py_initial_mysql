#coding:utf-8
from database import DB

class at_report():
    def __init__(self):
        self.record = DB('paic_reports','at_report')

    def select_by(self,**where):
        return [ at_report_Records(row) for row in self.record.select('idat_report','project','plan_on','report_date','passed','failed','pass_rate','last_updated','test_result').where(**where).submit() ]

class at_report_Records():
    def __init__(self,row):
        self.row = row

    @property
    def idat_report(self):
        return self.row[0]

    @property
    def project(self):
        return self.row[1]

    @property
    def plan_on(self):
        return self.row[2]

    @property
    def report_date(self):
        return self.row[3]

    @property
    def passed(self):
        return self.row[4]

    @property
    def failed(self):
        return self.row[5]

    @property
    def pass_rate(self):
        return self.row[6]

    @property
    def last_updated(self):
        return self.row[7]

    @property
    def test_result(self):
        return self.row[8]
