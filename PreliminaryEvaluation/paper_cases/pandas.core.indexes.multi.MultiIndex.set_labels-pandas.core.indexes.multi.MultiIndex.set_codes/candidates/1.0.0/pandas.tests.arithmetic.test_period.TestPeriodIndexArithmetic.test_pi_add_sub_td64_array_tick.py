def test_pi_add_sub_td64_array_tick(self):
    rng = pd.period_range('1/1/2000', freq='90D', periods=3)
    tdi = pd.TimedeltaIndex(['-1 Day', '-1 Day', '-1 Day'])
    tdarr = tdi.values
    expected = pd.period_range('12/31/1999', freq='90D', periods=3)
    result = rng + tdi
    tm.assert_index_equal(result, expected)
    result = rng + tdarr
    tm.assert_index_equal(result, expected)
    result = tdi + rng
    tm.assert_index_equal(result, expected)
    result = tdarr + rng
    tm.assert_index_equal(result, expected)
    expected = pd.period_range('1/2/2000', freq='90D', periods=3)
    result = rng - tdi
    tm.assert_index_equal(result, expected)
    result = rng - tdarr
    tm.assert_index_equal(result, expected)
    with pytest.raises(TypeError):
        tdarr - rng
    with pytest.raises(TypeError):
        tdi - rng