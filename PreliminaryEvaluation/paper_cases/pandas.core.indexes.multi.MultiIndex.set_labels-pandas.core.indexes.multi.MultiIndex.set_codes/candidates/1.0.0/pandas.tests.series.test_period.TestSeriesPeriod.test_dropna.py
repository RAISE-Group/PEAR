def test_dropna(self):
    s = Series([pd.Period('2011-01', freq='M'), pd.Period('NaT', freq='M')])
    tm.assert_series_equal(s.dropna(), Series([pd.Period('2011-01', freq='M')]))