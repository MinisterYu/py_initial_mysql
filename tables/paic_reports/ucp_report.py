#coding:utf-8
from database import DB

class ucp_report():
    def __init__(self):
        self.record = DB('paic_reports','ucp_report')

    def select_by(self,**where):
        return [ ucp_report_Records(row) for row in self.record.select('req_id','req_flag','req_series','req_name','req_brief','req_note','req_contactor','req_type','req_priority','req_developer','req_tester','req_process','req_com','created_date','created_by','updated_date','updated_by').where(**where).submit() ]

class ucp_report_Records():
    def __init__(self,row):
        self.row = row

    @property
    def req_id(self):
        return self.row[0]

    @property
    def req_flag(self):
        return self.row[1]

    @property
    def req_series(self):
        return self.row[2]

    @property
    def req_name(self):
        return self.row[3]

    @property
    def req_brief(self):
        return self.row[4]

    @property
    def req_note(self):
        return self.row[5]

    @property
    def req_contactor(self):
        return self.row[6]

    @property
    def req_type(self):
        return self.row[7]

    @property
    def req_priority(self):
        return self.row[8]

    @property
    def req_developer(self):
        return self.row[9]

    @property
    def req_tester(self):
        return self.row[10]

    @property
    def req_process(self):
        return self.row[11]

    @property
    def req_com(self):
        return self.row[12]

    @property
    def created_date(self):
        return self.row[13]

    @property
    def created_by(self):
        return self.row[14]

    @property
    def updated_date(self):
        return self.row[15]

    @property
    def updated_by(self):
        return self.row[16]
