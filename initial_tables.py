#! /usr/bin/env python
#coding:utf-8
from class_template import records_class,records_info,table_class

class AutoGenerator():

    def __init__(self,db):
        self.db = db
        self.class_name = 'reports'
        self.class_row= ['project','version','lamp','fixed']

        self.table = ''
        self.records = ''
        self.records_property = ''

        self._make_class()
        self._make_records_class()

    def _execute(self,sql):
        try:
            pass
        finally:
            pass

    def _get_tables_name(self):
        '''
        :return: tables name tuple
        '''
        return self.class_name

    def _get_table_rows_info(self):
        '''
        :return: table's struct tuple
        '''
        return self.class_row

    def _make_class(self):
        '''
        :return: make table class
        '''
        self.table = table_class.format(self.class_name,','.join(["'{0}'".format(i) for i in self.class_row]))

        return self.table

    def _make_records_class(self):
        '''
        :return: make table's rows class
        '''
        self.records = records_class.format(self.class_name)
        for i,row in enumerate(self.class_row):
            self.records_property += records_info.format(row,i)

        return self.records+self.records_property

    def export_file(self,file_path='./tables'):
        src = self.table+self.records+self.records_property
        print 'starting write db struct file:',self.class_name
        print  src
        with open('{0}/{1}.py'.format(file_path,self.class_name),'wb') as src_code:
            src_code.write(src)

        print 'generate file done...'

if __name__ == '__main__':
    it = AutoGenerator('paic')
    it.export_file()
