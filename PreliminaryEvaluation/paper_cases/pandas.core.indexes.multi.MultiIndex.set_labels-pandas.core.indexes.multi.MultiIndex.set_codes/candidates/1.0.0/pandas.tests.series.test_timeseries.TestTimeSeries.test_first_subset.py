def test_first_subset(self):
    ts = _simple_ts('1/1/2000', '1/1/2010', freq='12h')
    result = ts.first('10d')
    assert len(result) == 20
    ts = _simple_ts('1/1/2000', '1/1/2010')
    result = ts.first('10d')
    assert len(result) == 10
    result = ts.first('3M')
    expected = ts[:'3/31/2000']
    tm.assert_series_equal(result, expected)
    result = ts.first('21D')
    expected = ts[:21]
    tm.assert_series_equal(result, expected)
    result = ts[:0].first('3M')
    tm.assert_series_equal(result, ts[:0])