def test_ops_series_period(self):
    ser = pd.Series([pd.Period('2015-01-01', freq='D'), pd.Period('2015-01-02', freq='D')], name='xxx')
    assert ser.dtype == 'Period[D]'
    per = pd.Period('2015-01-10', freq='D')
    off = per.freq
    expected = pd.Series([9 * off, 8 * off], name='xxx', dtype=object)
    tm.assert_series_equal(per - ser, expected)
    tm.assert_series_equal(ser - per, -1 * expected)
    s2 = pd.Series([pd.Period('2015-01-05', freq='D'), pd.Period('2015-01-04', freq='D')], name='xxx')
    assert s2.dtype == 'Period[D]'
    expected = pd.Series([4 * off, 2 * off], name='xxx', dtype=object)
    tm.assert_series_equal(s2 - ser, expected)
    tm.assert_series_equal(ser - s2, -1 * expected)