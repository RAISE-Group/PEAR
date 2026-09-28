def test_constructor_timestamp_near_dst(self):
    ts = [Timestamp('2016-10-30 03:00:00+0300', tz='Europe/Helsinki'), Timestamp('2016-10-30 03:00:00+0200', tz='Europe/Helsinki')]
    result = DatetimeIndex(ts)
    expected = DatetimeIndex([ts[0].to_pydatetime(), ts[1].to_pydatetime()])
    tm.assert_index_equal(result, expected)