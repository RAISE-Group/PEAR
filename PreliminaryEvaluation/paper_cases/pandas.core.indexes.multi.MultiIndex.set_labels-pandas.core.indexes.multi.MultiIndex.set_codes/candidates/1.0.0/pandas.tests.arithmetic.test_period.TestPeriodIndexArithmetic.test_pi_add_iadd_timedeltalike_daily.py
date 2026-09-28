def test_pi_add_iadd_timedeltalike_daily(self, three_days):
    other = three_days
    rng = pd.period_range('2014-05-01', '2014-05-15', freq='D')
    expected = pd.period_range('2014-05-04', '2014-05-18', freq='D')
    result = rng + other
    tm.assert_index_equal(result, expected)
    rng += other
    tm.assert_index_equal(rng, expected)