def test_auto_conversion(self):
    series = Series(list(period_range('2000-01-01', periods=10, freq='D')))
    assert series.dtype == 'Period[D]'
    series = pd.Series([pd.Period('2011-01-01', freq='D'), pd.Period('2011-02-01', freq='D')])
    assert series.dtype == 'Period[D]'