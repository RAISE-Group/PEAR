def _to_sql(self, method=None):
    self.drop_table('test_frame1')
    self.pandasSQL.to_sql(self.test_frame1, 'test_frame1', method=method)
    assert self.pandasSQL.has_table('test_frame1')
    num_entries = len(self.test_frame1)
    num_rows = self._count_rows('test_frame1')
    assert num_rows == num_entries
    self.drop_table('test_frame1')