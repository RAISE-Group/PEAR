def test_quantile_nan(self):
    s = pd.Series([1, 2, 3, 4, np.nan])
    result = s.quantile(0.5)
    expected = 2.5
    assert result == expected
    s1 = Series([], dtype=object)
    cases = [s1, Series([np.nan, np.nan])]
    for s in cases:
        res = s.quantile(0.5)
        assert np.isnan(res)
        res = s.quantile([0.5])
        tm.assert_series_equal(res, pd.Series([np.nan], index=[0.5]))
        res = s.quantile([0.2, 0.3])
        tm.assert_series_equal(res, pd.Series([np.nan, np.nan], index=[0.2, 0.3]))