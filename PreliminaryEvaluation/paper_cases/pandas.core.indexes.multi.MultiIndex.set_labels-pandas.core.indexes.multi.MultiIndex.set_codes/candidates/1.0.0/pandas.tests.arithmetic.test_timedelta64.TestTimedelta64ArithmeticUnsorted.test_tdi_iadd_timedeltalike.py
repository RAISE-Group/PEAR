def test_tdi_iadd_timedeltalike(self, two_hours):
    rng = timedelta_range('1 days', '10 days')
    expected = timedelta_range('1 days 02:00:00', '10 days 02:00:00', freq='D')
    rng += two_hours
    tm.assert_index_equal(rng, expected)