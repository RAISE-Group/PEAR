def test_construct_with_different_start_end_string_format(self):
    result = date_range('2013-01-01 00:00:00+09:00', '2013/01/01 02:00:00+09:00', freq='H')
    expected = DatetimeIndex([Timestamp('2013-01-01 00:00:00+09:00'), Timestamp('2013-01-01 01:00:00+09:00'), Timestamp('2013-01-01 02:00:00+09:00')])
    tm.assert_index_equal(result, expected)