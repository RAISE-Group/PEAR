@pytest.mark.parametrize('freqstr', ['5ns', '5us', '5ms', '5s', '5T', '5h', '5d'])
def test_pi_add_timedeltalike_tick_gt1(self, three_days, freqstr):
    other = three_days
    rng = pd.period_range('2014-05-01', periods=6, freq=freqstr)
    expected = pd.period_range(rng[0] + other, periods=6, freq=freqstr)
    result = rng + other
    tm.assert_index_equal(result, expected)
    result = other + rng
    tm.assert_index_equal(result, expected)
    expected = pd.period_range(rng[0] - other, periods=6, freq=freqstr)
    result = rng - other
    tm.assert_index_equal(result, expected)
    with pytest.raises(TypeError):
        other - rng