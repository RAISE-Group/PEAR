def test_timedelta(self):
    df = to_timedelta(Series(['00:00:01', '00:00:03'], name='foo')).to_frame()
    with tm.assert_produces_warning(UserWarning):
        df.to_sql('test_timedelta', self.conn)
    result = sql.read_sql_query('SELECT * FROM test_timedelta', self.conn)
    tm.assert_series_equal(result['foo'], df['foo'].astype('int64'))