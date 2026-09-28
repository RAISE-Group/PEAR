def test_td64arr_add_timedeltalike(self, two_hours, box_with_array):
    box = box_with_array
    rng = timedelta_range('1 days', '10 days')
    expected = timedelta_range('1 days 02:00:00', '10 days 02:00:00', freq='D')
    rng = tm.box_expected(rng, box)
    expected = tm.box_expected(expected, box)
    result = rng + two_hours
    tm.assert_equal(result, expected)