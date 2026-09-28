def test_mixed_dtype(self):
    exp = Series(['foo'])
    s = Series([1, 'foo', 'foo'])
    tm.assert_series_equal(algos.mode(s), exp)