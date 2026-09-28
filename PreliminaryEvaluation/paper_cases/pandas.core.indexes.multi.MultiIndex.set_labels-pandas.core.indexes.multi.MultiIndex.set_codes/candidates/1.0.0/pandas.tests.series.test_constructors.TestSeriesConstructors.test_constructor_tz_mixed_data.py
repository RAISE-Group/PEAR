def test_constructor_tz_mixed_data(self):
    dt_list = [Timestamp('2016-05-01 02:03:37'), Timestamp('2016-04-30 19:03:37-0700', tz='US/Pacific')]
    result = Series(dt_list)
    expected = Series(dt_list, dtype=object)
    tm.assert_series_equal(result, expected)