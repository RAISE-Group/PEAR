def test_last_subset(self):
    ts = _simple_ts('1/1/2000', '1/1/2010', freq='12h')
    result = ts.last('10d')
    assert len(result) == 20
    ts = _simple_ts('1/1/2000', '1/1/2010')
    result = ts.last('10d')
    assert len(result) == 10
    result = ts.last('21D')
    expected = ts['12/12/2009':]
    tm.assert_series_equal(result, expected)
    result = ts.last('21D')
    expected = ts[-21:]
    tm.assert_series_equal(result, expected)
    result = ts[:0].last('3M')
    tm.assert_series_equal(result, ts[:0])