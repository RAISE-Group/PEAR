def test_pi_sub_isub_timedeltalike_daily(self, three_days):
    other = three_days
    rng = pd.period_range('2014-05-01', '2014-05-15', freq='D')
    expected = pd.period_range('2014-04-28', '2014-05-12', freq='D')
    result = rng - other
    tm.assert_index_equal(result, expected)
    rng -= other
    tm.assert_index_equal(rng, expected)