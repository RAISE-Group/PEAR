def test_datetime(self):
    df = DataFrame({'A': date_range('2013-01-01 09:00:00', periods=3), 'B': np.arange(3.0)})
    df.to_sql('test_datetime', self.conn)
    result = sql.read_sql_table('test_datetime', self.conn)
    result = result.drop('index', axis=1)
    tm.assert_frame_equal(result, df)
    result = sql.read_sql_query('SELECT * FROM test_datetime', self.conn)
    result = result.drop('index', axis=1)
    if self.flavor == 'sqlite':
        assert isinstance(result.loc[0, 'A'], str)
        result['A'] = to_datetime(result['A'])
        tm.assert_frame_equal(result, df)
    else:
        tm.assert_frame_equal(result, df)