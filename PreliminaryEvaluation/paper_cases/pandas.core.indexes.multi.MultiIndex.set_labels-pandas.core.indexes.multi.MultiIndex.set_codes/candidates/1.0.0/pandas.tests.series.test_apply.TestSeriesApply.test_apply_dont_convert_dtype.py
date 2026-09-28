def test_apply_dont_convert_dtype(self):
    s = Series(np.random.randn(10))
    f = lambda x: x if x > 0 else np.nan
    result = s.apply(f, convert_dtype=False)
    assert result.dtype == object