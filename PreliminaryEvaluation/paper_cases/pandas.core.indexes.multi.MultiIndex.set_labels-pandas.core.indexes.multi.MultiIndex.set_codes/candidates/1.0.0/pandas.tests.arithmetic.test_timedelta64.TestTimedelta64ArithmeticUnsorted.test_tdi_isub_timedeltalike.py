def test_tdi_isub_timedeltalike(self, two_hours):
    rng = timedelta_range('1 days', '10 days')
    expected = timedelta_range('0 days 22:00:00', '9 days 22:00:00')
    rng -= two_hours
    tm.assert_index_equal(rng, expected)