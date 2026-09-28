def _to_sql_empty(self):
    self.drop_table('test_frame1')
    self.pandasSQL.to_sql(self.test_frame1.iloc[:0], 'test_frame1')