def test_isna(self):
    s = Series([pd.Period('2011-01', freq='M'), pd.Period('NaT', freq='M')])
    tm.assert_series_equal(s.isna(), Series([False, True]))
    tm.assert_series_equal(s.notna(), Series([True, False]))