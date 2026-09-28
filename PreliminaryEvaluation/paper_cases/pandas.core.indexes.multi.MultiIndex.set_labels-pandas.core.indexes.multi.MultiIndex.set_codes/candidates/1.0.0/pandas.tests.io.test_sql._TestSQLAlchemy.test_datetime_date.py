def test_datetime_date(self):
    df = DataFrame([date(2014, 1, 1), date(2014, 1, 2)], columns=['a'])
    df.to_sql('test_date', self.conn, index=False)
    res = read_sql_table('test_date', self.conn)
    result = res['a']
    expected = to_datetime(df['a'])
    tm.assert_series_equal(result, expected)