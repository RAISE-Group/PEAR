def test_comparisons(self):
    left = np.random.randn(10)
    right = np.random.randn(10)
    left[:3] = np.nan
    result = nanops.nangt(left, right)
    with np.errstate(invalid='ignore'):
        expected = (left > right).astype('O')
    expected[:3] = np.nan
    tm.assert_almost_equal(result, expected)
    s = Series(['a', 'b', 'c'])
    s2 = Series([False, True, False])
    exp = Series([False, False, False])
    tm.assert_series_equal(s == s2, exp)
    tm.assert_series_equal(s2 == s, exp)