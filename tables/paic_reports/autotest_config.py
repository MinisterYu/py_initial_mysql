#coding:utf-8
from database import DB

class autotest_config():
    def __init__(self):
        self.record = DB('paic_reports','autotest_config')

    def select_by(self,**where):
        return [ autotest_config_Records(row) for row in self.record.select('id','project','host','test_suite','test_include','test_exclude','test_schedule','created_date','created_by','updated_date','updated_by').where(**where).submit() ]

class autotest_config_Records():
    def __init__(self,row):
        self.row = row

    @property
    def id(self):
        return self.row[0]

    @property
    def project(self):
        return self.row[1]

    @property
    def host(self):
        return self.row[2]

    @property
    def test_suite(self):
        return self.row[3]

    @property
    def test_include(self):
        return self.row[4]

    @property
    def test_exclude(self):
        return self.row[5]

    @property
    def test_schedule(self):
        return self.row[6]

    @property
    def created_date(self):
        return self.row[7]

    @property
    def created_by(self):
        return self.row[8]

    @property
    def updated_date(self):
        return self.row[9]

    @property
    def updated_by(self):
        return self.row[10]
