#! /usr/bin/env python
#coding:utf-8
from template import records_class,records_info,table_class
from database import HANDLE

class AutoGenerator():

    def __init__(self,db):
        self.db = db
        self.class_name_sql = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'paic_reports'"
        self.class_row_sql = "SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE table_name = '{0}';"

    def _execute(self,sql):
        handle = HANDLE(self.db,sql)
        return handle.submit()

    def _get_tables_name(self):
        '''
        :return: tables name tuple
        '''
        self.class_name = self._execute(self.class_name_sql)
        return self.class_name

    def _get_table_rows_info(self,table):
        '''
        :return: table's struct tuple
        '''
        self.class_row = self._execute(self.class_row_sql.format(table))
        return self.class_row

    def _make_class(self,table):
        '''
        :return: make table class
        '''
        self.table = ''
        self.table = table_class.format(self.db,table,','.join(["'{0}'".format(i[0]) for i in self.class_row]))

        return self.table

    def _make_records_class(self,table):
        '''
        :return: make table's rows class
        '''
        self.records = ''
        self.records_property = ''
        self.records = records_class.format(table)
        for i,row in enumerate(self.class_row):
            self.records_property += records_info.format(row[0],i)

        return self.records+self.records_property

    def export_file(self,file_path='tables'):
        tables = self._get_tables_name()
        src_path = './{0}/{1}'.format(file_path,self.db)

        with open('{0}/__init__.py'.format(src_path), 'wb') as src:
            src.write('')
        for table in tables:
            table = table[0]
            rows = self._get_table_rows_info(table)
            self._make_class(table)
            self._make_records_class(table)
            src_code = self.table+self.records+self.records_property
            print 'starting write db struct file:',table
            with open('{0}/{1}.py'.format(src_path,table),'wb') as src:
                src.write(src_code)
        print 'generate file done...'

if __name__ == '__main__':
    it = AutoGenerator('paic_reports')
    it.export_file()
