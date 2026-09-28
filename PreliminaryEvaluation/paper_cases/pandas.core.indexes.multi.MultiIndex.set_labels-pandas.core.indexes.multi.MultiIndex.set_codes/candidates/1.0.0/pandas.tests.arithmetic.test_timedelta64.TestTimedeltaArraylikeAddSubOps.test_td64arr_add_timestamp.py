def test_td64arr_add_timestamp(self, box_with_array, tz_naive_fixture):
    tz = tz_naive_fixture
    other = Timestamp('2011-01-01', tz=tz)
    idx = TimedeltaIndex(['1 day', '2 day'])
    expected = DatetimeIndex(['2011-01-02', '2011-01-03'], tz=tz)
    idx = tm.box_expected(idx, box_with_array)
    expected = tm.box_expected(expected, box_with_array)
    result = idx + other
    tm.assert_equal(result, expected)
    result = other + idx
    tm.assert_equal(result, expected)