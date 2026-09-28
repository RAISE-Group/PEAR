def test_to_sql_type_mapping(self):
    sql.to_sql(self.test_frame3, 'test_frame5', self.conn, index=False)
    result = sql.read_sql('SELECT * FROM test_frame5', self.conn)
    tm.assert_frame_equal(self.test_frame3, result)