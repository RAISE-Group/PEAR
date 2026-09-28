def test_pi_sub_isub_pi(self):
    rng = pd.period_range('1/1/2000', freq='D', periods=5)
    other = pd.period_range('1/6/2000', freq='D', periods=5)
    off = rng.freq
    expected = pd.Index([-5 * off] * 5)
    result = rng - other
    tm.assert_index_equal(result, expected)
    rng -= other
    tm.assert_index_equal(rng, expected)