def test_datetime_with_timezone_roundtrip(self):
    expected = DataFrame({'A': date_range('2013-01-01 09:00:00', periods=3, tz='US/Pacific')})
    expected.to_sql('test_datetime_tz', self.conn, index=False)
    if self.flavor == 'postgresql':
        expected['A'] = expected['A'].dt.tz_convert('UTC')
    else:
        expected['A'] = expected['A'].dt.tz_localize(None)
    result = sql.read_sql_table('test_datetime_tz', self.conn)
    tm.assert_frame_equal(result, expected)
    result = sql.read_sql_query('SELECT * FROM test_datetime_tz', self.conn)
    if self.flavor == 'sqlite':
        assert isinstance(result.loc[0, 'A'], str)
        result['A'] = to_datetime(result['A'])
    tm.assert_frame_equal(result, expected)