def test_datetime_date(self):
    df = DataFrame([date(2014, 1, 1), date(2014, 1, 2)], columns=['a'])
    df.to_sql('test_date', self.conn, index=False)
    res = read_sql_query('SELECT * FROM test_date', self.conn)
    if self.flavor == 'sqlite':
        tm.assert_frame_equal(res, df.astype(str))
    elif self.flavor == 'mysql':
        tm.assert_frame_equal(res, df)