def test_append_concat(self):
    d1 = date_range('12/31/1990', '12/31/1999', freq='A-DEC')
    d2 = date_range('12/31/2000', '12/31/2009', freq='A-DEC')
    s1 = Series(np.random.randn(10), d1)
    s2 = Series(np.random.randn(10), d2)
    s1 = s1.to_period()
    s2 = s2.to_period()
    result = pd.concat([s1, s2])
    assert isinstance(result.index, PeriodIndex)
    assert result.index[0] == s1.index[0]