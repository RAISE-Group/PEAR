def test_getitem(self):
    assert self.series[1] == pd.Period('2000-01-02', freq='D')
    result = self.series[[2, 4]]
    exp = pd.Series([pd.Period('2000-01-03', freq='D'), pd.Period('2000-01-05', freq='D')], index=[2, 4], dtype='Period[D]')
    tm.assert_series_equal(result, exp)
    assert result.dtype == 'Period[D]'