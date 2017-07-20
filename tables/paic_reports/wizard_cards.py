#coding:utf-8
from database import DB

class wizard_cards():
    def __init__(self):
        self.record = DB('paic_reports','wizard_cards')

    def select_by(self,**where):
        return [ wizard_cards_Records(row) for row in self.record.select('unid','project_id','plan_id','card_id','card_seq','card_type','title','description','developer','developer_id','tester','tester_id','busitype','busimode','busiseries','priority','priority_id','state','state_id','contactor','due_date','blocked','is_deleted','note','created_time','updated_time').where(**where).submit() ]

class wizard_cards_Records():
    def __init__(self,row):
        self.row = row

    @property
    def unid(self):
        return self.row[0]

    @property
    def project_id(self):
        return self.row[1]

    @property
    def plan_id(self):
        return self.row[2]

    @property
    def card_id(self):
        return self.row[3]

    @property
    def card_seq(self):
        return self.row[4]

    @property
    def card_type(self):
        return self.row[5]

    @property
    def title(self):
        return self.row[6]

    @property
    def description(self):
        return self.row[7]

    @property
    def developer(self):
        return self.row[8]

    @property
    def developer_id(self):
        return self.row[9]

    @property
    def tester(self):
        return self.row[10]

    @property
    def tester_id(self):
        return self.row[11]

    @property
    def busitype(self):
        return self.row[12]

    @property
    def busimode(self):
        return self.row[13]

    @property
    def busiseries(self):
        return self.row[14]

    @property
    def priority(self):
        return self.row[15]

    @property
    def priority_id(self):
        return self.row[16]

    @property
    def state(self):
        return self.row[17]

    @property
    def state_id(self):
        return self.row[18]

    @property
    def contactor(self):
        return self.row[19]

    @property
    def due_date(self):
        return self.row[20]

    @property
    def blocked(self):
        return self.row[21]

    @property
    def is_deleted(self):
        return self.row[22]

    @property
    def note(self):
        return self.row[23]

    @property
    def created_time(self):
        return self.row[24]

    @property
    def updated_time(self):
        return self.row[25]
