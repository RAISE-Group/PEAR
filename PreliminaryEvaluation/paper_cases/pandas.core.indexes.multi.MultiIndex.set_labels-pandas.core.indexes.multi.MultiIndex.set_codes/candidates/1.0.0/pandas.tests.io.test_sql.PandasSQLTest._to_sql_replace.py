def _to_sql_replace(self):
    self.drop_table('test_frame1')
    self.pandasSQL.to_sql(self.test_frame1, 'test_frame1', if_exists='fail')
    self.pandasSQL.to_sql(self.test_frame1, 'test_frame1', if_exists='replace')
    assert self.pandasSQL.has_table('test_frame1')
    num_entries = len(self.test_frame1)
    num_rows = self._count_rows('test_frame1')
    assert num_rows == num_entries
    self.drop_table('test_frame1')