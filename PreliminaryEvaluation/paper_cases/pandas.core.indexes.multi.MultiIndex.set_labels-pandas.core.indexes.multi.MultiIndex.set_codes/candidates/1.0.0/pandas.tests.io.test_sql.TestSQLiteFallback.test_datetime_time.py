def test_datetime_time(self):
    df = DataFrame([time(9, 0, 0), time(9, 1, 30)], columns=['a'])
    df.to_sql('test_time', self.conn, index=False)
    res = read_sql_query('SELECT * FROM test_time', self.conn)
    if self.flavor == 'sqlite':
        expected = df.applymap(lambda _: _.strftime('%H:%M:%S.%f'))
        tm.assert_frame_equal(res, expected)