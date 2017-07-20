#coding:utf-8
from database import DB

class ci_nodes():
    def __init__(self):
        self.record = DB('paic_reports','ci_nodes')

    def select_by(self,**where):
        return [ ci_nodes_Records(row) for row in self.record.select('id_nodes','name','status','max','comment','workspace','date_created','date_updated').where(**where).submit() ]

class ci_nodes_Records():
    def __init__(self,row):
        self.row = row

    @property
    def id_nodes(self):
        return self.row[0]

    @property
    def name(self):
        return self.row[1]

    @property
    def status(self):
        return self.row[2]

    @property
    def max(self):
        return self.row[3]

    @property
    def comment(self):
        return self.row[4]

    @property
    def workspace(self):
        return self.row[5]

    @property
    def date_created(self):
        return self.row[6]

    @property
    def date_updated(self):
        return self.row[7]
