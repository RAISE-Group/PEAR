def test_nan_numeric(self):
    df = DataFrame({'A': [0, 1, 2], 'B': [0.2, np.nan, 5.6]})
    df.to_sql('test_nan', self.conn, index=False)
    result = sql.read_sql_table('test_nan', self.conn)
    tm.assert_frame_equal(result, df)
    result = sql.read_sql_query('SELECT * FROM test_nan', self.conn)
    tm.assert_frame_equal(result, df)