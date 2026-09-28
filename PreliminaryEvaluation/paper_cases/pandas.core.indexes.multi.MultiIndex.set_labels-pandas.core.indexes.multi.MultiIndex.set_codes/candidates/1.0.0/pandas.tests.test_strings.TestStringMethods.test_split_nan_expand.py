def test_split_nan_expand(self):
    s = Series(['foo,bar,baz', np.nan])
    result = s.str.split(',', expand=True)
    exp = DataFrame([['foo', 'bar', 'baz'], [np.nan, np.nan, np.nan]])
    tm.assert_frame_equal(result, exp)
    assert all((np.isnan(x) for x in result.iloc[1]))