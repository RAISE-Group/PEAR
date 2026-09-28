def test_nan_fullcolumn(self):
    df = DataFrame({'A': [0, 1, 2], 'B': [np.nan, np.nan, np.nan]})
    df.to_sql('test_nan', self.conn, index=False)
    result = sql.read_sql_table('test_nan', self.conn)
    tm.assert_frame_equal(result, df)
    df['B'] = df['B'].astype('object')
    df['B'] = None
    result = sql.read_sql_query('SELECT * FROM test_nan', self.conn)
    tm.assert_frame_equal(result, df)