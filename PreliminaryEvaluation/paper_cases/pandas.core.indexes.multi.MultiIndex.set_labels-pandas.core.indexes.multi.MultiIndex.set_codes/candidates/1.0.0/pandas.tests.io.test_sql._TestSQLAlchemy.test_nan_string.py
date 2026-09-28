def test_nan_string(self):
    df = DataFrame({'A': [0, 1, 2], 'B': ['a', 'b', np.nan]})
    df.to_sql('test_nan', self.conn, index=False)
    df.loc[2, 'B'] = None
    result = sql.read_sql_table('test_nan', self.conn)
    tm.assert_frame_equal(result, df)
    result = sql.read_sql_query('SELECT * FROM test_nan', self.conn)
    tm.assert_frame_equal(result, df)