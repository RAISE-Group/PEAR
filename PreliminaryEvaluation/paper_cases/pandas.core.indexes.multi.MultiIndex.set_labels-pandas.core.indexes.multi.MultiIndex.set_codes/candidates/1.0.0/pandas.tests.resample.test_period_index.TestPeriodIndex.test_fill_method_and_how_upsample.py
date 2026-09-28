def test_fill_method_and_how_upsample(self):
    s = Series(np.arange(9, dtype='int64'), index=date_range('2010-01-01', periods=9, freq='Q'))
    last = s.resample('M').ffill()
    both = s.resample('M').ffill().resample('M').last().astype('int64')
    tm.assert_series_equal(last, both)