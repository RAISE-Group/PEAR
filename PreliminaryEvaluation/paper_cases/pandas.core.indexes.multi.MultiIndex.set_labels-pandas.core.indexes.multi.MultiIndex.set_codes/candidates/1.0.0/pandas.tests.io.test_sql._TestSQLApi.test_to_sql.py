def test_to_sql(self):
    sql.to_sql(self.test_frame1, 'test_frame1', self.conn)
    assert sql.has_table('test_frame1', self.conn)