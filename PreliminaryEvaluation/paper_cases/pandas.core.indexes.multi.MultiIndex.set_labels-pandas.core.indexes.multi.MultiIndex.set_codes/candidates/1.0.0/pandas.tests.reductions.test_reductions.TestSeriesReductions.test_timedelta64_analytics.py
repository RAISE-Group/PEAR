def test_timedelta64_analytics(self):
    dti = pd.date_range('2012-1-1', periods=3, freq='D')
    td = Series(dti) - pd.Timestamp('20120101')
    result = td.idxmin()
    assert result == 0
    result = td.idxmax()
    assert result == 2
    td[0] = np.nan
    result = td.idxmin()
    assert result == 1
    result = td.idxmax()
    assert result == 2
    s1 = Series(pd.date_range('20120101', periods=3))
    s2 = Series(pd.date_range('20120102', periods=3))
    expected = Series(s2 - s1)
    result = (s1 - s2).abs()
    tm.assert_series_equal(result, expected)
    result = td.max()
    expected = pd.Timedelta('2 days')
    assert result == expected
    result = td.min()
    expected = pd.Timedelta('1 days')
    assert result == expected