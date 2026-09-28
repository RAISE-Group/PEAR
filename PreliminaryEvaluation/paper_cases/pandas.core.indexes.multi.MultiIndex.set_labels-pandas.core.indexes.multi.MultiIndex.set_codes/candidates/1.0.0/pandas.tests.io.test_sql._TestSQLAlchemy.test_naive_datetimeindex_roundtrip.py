def test_naive_datetimeindex_roundtrip(self):
    dates = date_range('2018-01-01', periods=5, freq='6H')
    expected = DataFrame({'nums': range(5)}, index=dates)
    expected.to_sql('foo_table', self.conn, index_label='info_date')
    result = sql.read_sql_table('foo_table', self.conn, index_col='info_date')
    tm.assert_frame_equal(result, expected, check_names=False)