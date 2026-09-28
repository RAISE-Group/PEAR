def test_roundtrip_chunksize(self):
    sql.to_sql(self.test_frame1, 'test_frame_roundtrip', con=self.conn, index=False, chunksize=2)
    result = sql.read_sql_query('SELECT * FROM test_frame_roundtrip', con=self.conn)
    tm.assert_frame_equal(result, self.test_frame1)