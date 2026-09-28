def test_comparison_flex_basic(self):
    left = pd.Series(np.random.randn(10))
    right = pd.Series(np.random.randn(10))
    tm.assert_series_equal(left.eq(right), left == right)
    tm.assert_series_equal(left.ne(right), left != right)
    tm.assert_series_equal(left.le(right), left < right)
    tm.assert_series_equal(left.lt(right), left <= right)
    tm.assert_series_equal(left.gt(right), left > right)
    tm.assert_series_equal(left.ge(right), left >= right)
    for axis in [0, None, 'index']:
        tm.assert_series_equal(left.eq(right, axis=axis), left == right)
        tm.assert_series_equal(left.ne(right, axis=axis), left != right)
        tm.assert_series_equal(left.le(right, axis=axis), left < right)
        tm.assert_series_equal(left.lt(right, axis=axis), left <= right)
        tm.assert_series_equal(left.gt(right, axis=axis), left > right)
        tm.assert_series_equal(left.ge(right, axis=axis), left >= right)
    msg = 'No axis named 1 for object type'
    for op in ['eq', 'ne', 'le', 'le', 'gt', 'ge']:
        with pytest.raises(ValueError, match=msg):
            getattr(left, op)(right, axis=1)