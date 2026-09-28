def test_pi_sub_isub_timedeltalike_hourly(self, two_hours):
    other = two_hours
    rng = pd.period_range('2014-01-01 10:00', '2014-01-05 10:00', freq='H')
    expected = pd.period_range('2014-01-01 08:00', '2014-01-05 08:00', freq='H')
    result = rng - other
    tm.assert_index_equal(result, expected)
    rng -= other
    tm.assert_index_equal(rng, expected)