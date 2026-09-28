def test_between(self):
    s = Series(bdate_range('1/1/2000', periods=20).astype(object))
    s[::2] = np.nan
    result = s[s.between(s[3], s[17])]
    expected = s[3:18].dropna()
    tm.assert_series_equal(result, expected)
    result = s[s.between(s[3], s[17], inclusive=False)]
    expected = s[5:16].dropna()
    tm.assert_series_equal(result, expected)