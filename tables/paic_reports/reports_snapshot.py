#coding:utf-8
from database import DB

class reports_snapshot():
    def __init__(self):
        self.record = DB('paic_reports','reports_snapshot')

    def select_by(self,**where):
        return [ reports_snapshot_Records(row) for row in self.record.select('captrue_id','captrue_date','reports_id','project','version','principal_code','first_deploy','release_date','sr','executes','pass_rate','bugs','fixed','is_rollback_code','is_test_rollback_code','risk','note','status_code','created_date','created_by','updated_date','updated_by').where(**where).submit() ]

class reports_snapshot_Records():
    def __init__(self,row):
        self.row = row

    @property
    def captrue_id(self):
        return self.row[0]

    @property
    def captrue_date(self):
        return self.row[1]

    @property
    def reports_id(self):
        return self.row[2]

    @property
    def project(self):
        return self.row[3]

    @property
    def version(self):
        return self.row[4]

    @property
    def principal_code(self):
        return self.row[5]

    @property
    def first_deploy(self):
        return self.row[6]

    @property
    def release_date(self):
        return self.row[7]

    @property
    def sr(self):
        return self.row[8]

    @property
    def executes(self):
        return self.row[9]

    @property
    def pass_rate(self):
        return self.row[10]

    @property
    def bugs(self):
        return self.row[11]

    @property
    def fixed(self):
        return self.row[12]

    @property
    def is_rollback_code(self):
        return self.row[13]

    @property
    def is_test_rollback_code(self):
        return self.row[14]

    @property
    def risk(self):
        return self.row[15]

    @property
    def note(self):
        return self.row[16]

    @property
    def status_code(self):
        return self.row[17]

    @property
    def created_date(self):
        return self.row[18]

    @property
    def created_by(self):
        return self.row[19]

    @property
    def updated_date(self):
        return self.row[20]

    @property
    def updated_by(self):
        return self.row[21]
