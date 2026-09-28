def test_constructor_scalar(self):
    idx = Index(range(3))
    df = DataFrame({'a': 0}, index=idx)
    expected = DataFrame({'a': [0, 0, 0]}, index=idx)
    tm.assert_frame_equal(df, expected, check_dtype=False)