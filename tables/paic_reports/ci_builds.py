#coding:utf-8
from database import DB

class ci_builds():
    def __init__(self):
        self.record = DB('paic_reports','ci_builds')

    def select_by(self,**where):
        return [ ci_builds_Records(row) for row in self.record.select('id_builds','id_jobs','build_numbers','build_elapse','build_date','build_manual','build_at','build_coverage','build_success','build_skip','build_failed','build_result','build_built_on','build_su_rate','build_log_url','failed_reason','failed_comment','date_created','date_updated').where(**where).submit() ]

class ci_builds_Records():
    def __init__(self,row):
        self.row = row

    @property
    def id_builds(self):
        return self.row[0]

    @property
    def id_jobs(self):
        return self.row[1]

    @property
    def build_numbers(self):
        return self.row[2]

    @property
    def build_elapse(self):
        return self.row[3]

    @property
    def build_date(self):
        return self.row[4]

    @property
    def build_manual(self):
        return self.row[5]

    @property
    def build_at(self):
        return self.row[6]

    @property
    def build_coverage(self):
        return self.row[7]

    @property
    def build_success(self):
        return self.row[8]

    @property
    def build_skip(self):
        return self.row[9]

    @property
    def build_failed(self):
        return self.row[10]

    @property
    def build_result(self):
        return self.row[11]

    @property
    def build_built_on(self):
        return self.row[12]

    @property
    def build_su_rate(self):
        return self.row[13]

    @property
    def build_log_url(self):
        return self.row[14]

    @property
    def failed_reason(self):
        return self.row[15]

    @property
    def failed_comment(self):
        return self.row[16]

    @property
    def date_created(self):
        return self.row[17]

    @property
    def date_updated(self):
        return self.row[18]
