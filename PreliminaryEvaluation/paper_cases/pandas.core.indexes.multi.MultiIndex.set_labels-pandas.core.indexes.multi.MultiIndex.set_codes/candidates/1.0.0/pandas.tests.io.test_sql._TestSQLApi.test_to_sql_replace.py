def test_to_sql_replace(self):
    sql.to_sql(self.test_frame1, 'test_frame3', self.conn, if_exists='fail')
    sql.to_sql(self.test_frame1, 'test_frame3', self.conn, if_exists='replace')
    assert sql.has_table('test_frame3', self.conn)
    num_entries = len(self.test_frame1)
    num_rows = self._count_rows('test_frame3')
    assert num_rows == num_entries