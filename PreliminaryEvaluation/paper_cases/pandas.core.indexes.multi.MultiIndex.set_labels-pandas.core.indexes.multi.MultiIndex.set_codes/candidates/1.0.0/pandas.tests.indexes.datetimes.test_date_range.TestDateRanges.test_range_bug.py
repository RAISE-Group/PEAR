def test_range_bug(self):
    offset = DateOffset(months=3)
    result = date_range('2011-1-1', '2012-1-31', freq=offset)
    start = datetime(2011, 1, 1)
    expected = DatetimeIndex([start + i * offset for i in range(5)])
    tm.assert_index_equal(result, expected)