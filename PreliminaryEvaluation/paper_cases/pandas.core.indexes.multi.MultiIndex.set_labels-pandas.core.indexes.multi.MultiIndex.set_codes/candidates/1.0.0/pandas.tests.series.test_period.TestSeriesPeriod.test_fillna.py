def test_fillna(self):
    s = Series([pd.Period('2011-01', freq='M'), pd.Period('NaT', freq='M')])
    res = s.fillna(pd.Period('2012-01', freq='M'))
    exp = Series([pd.Period('2011-01', freq='M'), pd.Period('2012-01', freq='M')])
    tm.assert_series_equal(res, exp)
    assert res.dtype == 'Period[M]'