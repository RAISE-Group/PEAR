def test_to_sql_append(self):
    sql.to_sql(self.test_frame1, 'test_frame4', self.conn, if_exists='fail')
    sql.to_sql(self.test_frame1, 'test_frame4', self.conn, if_exists='append')
    assert sql.has_table('test_frame4', self.conn)
    num_entries = 2 * len(self.test_frame1)
    num_rows = self._count_rows('test_frame4')
    assert num_rows == num_entries