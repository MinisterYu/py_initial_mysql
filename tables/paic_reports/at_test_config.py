#coding:utf-8
from database import DB

class at_test_config():
    def __init__(self):
        self.record = DB('paic_reports','at_test_config')

    def select_by(self,**where):
        return [ at_test_config_Records(row) for row in self.record.select('id','project','token','plan_on','test_type','test_host','test_suite','test_include','test_exclude','created_by','created_date','updated_by','updated_date').where(**where).submit() ]

class at_test_config_Records():
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
    def test_type(self):
        return self.row[4]

    @property
    def test_host(self):
        return self.row[5]

    @property
    def test_suite(self):
        return self.row[6]

    @property
    def test_include(self):
        return self.row[7]

    @property
    def test_exclude(self):
        return self.row[8]

    @property
    def created_by(self):
        return self.row[9]

    @property
    def created_date(self):
        return self.row[10]

    @property
    def updated_by(self):
        return self.row[11]

    @property
    def updated_date(self):
        return self.row[12]
