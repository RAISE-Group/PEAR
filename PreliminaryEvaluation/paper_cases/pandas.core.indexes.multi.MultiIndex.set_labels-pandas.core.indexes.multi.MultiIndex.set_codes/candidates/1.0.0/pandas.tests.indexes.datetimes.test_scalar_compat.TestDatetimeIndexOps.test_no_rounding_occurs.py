def test_no_rounding_occurs(self, tz_naive_fixture):
    tz = tz_naive_fixture
    rng = date_range(start='2016-01-01', periods=5, freq='2Min', tz=tz)
    expected_rng = DatetimeIndex([Timestamp('2016-01-01 00:00:00', tz=tz, freq='2T'), Timestamp('2016-01-01 00:02:00', tz=tz, freq='2T'), Timestamp('2016-01-01 00:04:00', tz=tz, freq='2T'), Timestamp('2016-01-01 00:06:00', tz=tz, freq='2T'), Timestamp('2016-01-01 00:08:00', tz=tz, freq='2T')])
    tm.assert_index_equal(rng.round(freq='2T'), expected_rng)