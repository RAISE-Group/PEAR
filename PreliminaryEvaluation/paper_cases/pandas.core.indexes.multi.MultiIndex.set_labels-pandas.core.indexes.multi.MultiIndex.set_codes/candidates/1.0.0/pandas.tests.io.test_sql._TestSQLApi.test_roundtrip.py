def test_roundtrip(self):
    sql.to_sql(self.test_frame1, 'test_frame_roundtrip', con=self.conn)
    result = sql.read_sql_query('SELECT * FROM test_frame_roundtrip', con=self.conn)
    result.index = self.test_frame1.index
    result.set_index('level_0', inplace=True)
    result.index.astype(int)
    result.index.name = None
    tm.assert_frame_equal(result, self.test_frame1)