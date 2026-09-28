def test_fillna_downcast(self):
    s = pd.Series([1.0, np.nan])
    result = s.fillna(0, downcast='infer')
    expected = pd.Series([1, 0])
    tm.assert_series_equal(result, expected)
    s = pd.Series([1.0, np.nan])
    result = s.fillna({1: 0}, downcast='infer')
    expected = pd.Series([1, 0])
    tm.assert_series_equal(result, expected)