def test_pi_sub_pi_with_nat(self):
    rng = pd.period_range('1/1/2000', freq='D', periods=5)
    other = rng[1:].insert(0, pd.NaT)
    assert other[1:].equals(rng[1:])
    result = rng - other
    off = rng.freq
    expected = pd.Index([pd.NaT, 0 * off, 0 * off, 0 * off, 0 * off])
    tm.assert_index_equal(result, expected)