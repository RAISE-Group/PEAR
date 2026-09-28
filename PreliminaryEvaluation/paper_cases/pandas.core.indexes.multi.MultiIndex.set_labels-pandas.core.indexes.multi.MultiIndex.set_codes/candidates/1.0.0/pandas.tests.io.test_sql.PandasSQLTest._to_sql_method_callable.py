def _to_sql_method_callable(self):
    check = []

    def sample(pd_table, conn, keys, data_iter):
        check.append(1)
        data = [dict(zip(keys, row)) for row in data_iter]
        conn.execute(pd_table.table.insert(), data)
    self.drop_table('test_frame1')
    self.pandasSQL.to_sql(self.test_frame1, 'test_frame1', method=sample)
    assert self.pandasSQL.has_table('test_frame1')
    assert check == [1]
    num_entries = len(self.test_frame1)
    num_rows = self._count_rows('test_frame1')
    assert num_rows == num_entries
    self.drop_table('test_frame1')