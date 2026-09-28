def test_pi_add_timedeltalike_minute_gt1(self, three_days):
    other = three_days
    rng = pd.period_range('2014-05-01', periods=3, freq='2D')
    expected = pd.PeriodIndex(['2014-05-04', '2014-05-06', '2014-05-08'], freq='2D')
    result = rng + other
    tm.assert_index_equal(result, expected)
    result = other + rng
    tm.assert_index_equal(result, expected)
    expected = pd.PeriodIndex(['2014-04-28', '2014-04-30', '2014-05-02'], freq='2D')
    result = rng - other
    tm.assert_index_equal(result, expected)
    with pytest.raises(TypeError):
        other - rng