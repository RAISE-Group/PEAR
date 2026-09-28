def test_dropna_no_nan(self):
    for s in [Series([1, 2, 3], name='x'), Series([False, True, False], name='x')]:
        result = s.dropna()
        tm.assert_series_equal(result, s)
        assert result is not s
        s2 = s.copy()
        s2.dropna(inplace=True)
        tm.assert_series_equal(s2, s)