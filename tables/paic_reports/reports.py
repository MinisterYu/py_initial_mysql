#coding:utf-8
from database import DB

class reports():
    def __init__(self):
        self.record = DB('paic_reports','reports')

    def select_by(self,**where):
        return [ reports_Records(row) for row in self.record.select('reports_id','project','version','lamp','principal_code','first_deploy','release_date','sr','executes','pass_rate','bugs','bugs_for_developer','bugs_for_tester','tester_bugs_lamp','developer_bugs_lamp','fixed','is_rollback_code','rollback_strategy','is_test_rollback_code','rollback_spendtime','risk','note','compatibility','performance','status_code','link','created_date','created_by','updated_date','updated_by').where(**where).submit() ]

class reports_Records():
    def __init__(self,row):
        self.row = row

    @property
    def reports_id(self):
        return self.row[0]

    @property
    def project(self):
        return self.row[1]

    @property
    def version(self):
        return self.row[2]

    @property
    def lamp(self):
        return self.row[3]

    @property
    def principal_code(self):
        return self.row[4]

    @property
    def first_deploy(self):
        return self.row[5]

    @property
    def release_date(self):
        return self.row[6]

    @property
    def sr(self):
        return self.row[7]

    @property
    def executes(self):
        return self.row[8]

    @property
    def pass_rate(self):
        return self.row[9]

    @property
    def bugs(self):
        return self.row[10]

    @property
    def bugs_for_developer(self):
        return self.row[11]

    @property
    def bugs_for_tester(self):
        return self.row[12]

    @property
    def tester_bugs_lamp(self):
        return self.row[13]

    @property
    def developer_bugs_lamp(self):
        return self.row[14]

    @property
    def fixed(self):
        return self.row[15]

    @property
    def is_rollback_code(self):
        return self.row[16]

    @property
    def rollback_strategy(self):
        return self.row[17]

    @property
    def is_test_rollback_code(self):
        return self.row[18]

    @property
    def rollback_spendtime(self):
        return self.row[19]

    @property
    def risk(self):
        return self.row[20]

    @property
    def note(self):
        return self.row[21]

    @property
    def compatibility(self):
        return self.row[22]

    @property
    def performance(self):
        return self.row[23]

    @property
    def status_code(self):
        return self.row[24]

    @property
    def link(self):
        return self.row[25]

    @property
    def created_date(self):
        return self.row[26]

    @property
    def created_by(self):
        return self.row[27]

    @property
    def updated_date(self):
        return self.row[28]

    @property
    def updated_by(self):
        return self.row[29]
