def test_date_range_convenience_periods(self):
    result = date_range('2018-04-24', '2018-04-27', periods=3)
    expected = DatetimeIndex(['2018-04-24 00:00:00', '2018-04-25 12:00:00', '2018-04-27 00:00:00'], freq=None)
    tm.assert_index_equal(result, expected)
    result = date_range('2018-04-01 01:00:00', '2018-04-01 04:00:00', tz='Australia/Sydney', periods=3)
    expected = DatetimeIndex([Timestamp('2018-04-01 01:00:00+1100', tz='Australia/Sydney'), Timestamp('2018-04-01 02:00:00+1000', tz='Australia/Sydney'), Timestamp('2018-04-01 04:00:00+1000', tz='Australia/Sydney')])
    tm.assert_index_equal(result, expected)