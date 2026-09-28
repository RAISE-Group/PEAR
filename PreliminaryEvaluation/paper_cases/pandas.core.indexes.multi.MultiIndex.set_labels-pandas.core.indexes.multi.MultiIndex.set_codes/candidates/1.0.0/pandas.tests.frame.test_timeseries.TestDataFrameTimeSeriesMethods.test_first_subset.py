def test_first_subset(self):
    ts = tm.makeTimeDataFrame(freq='12h')
    result = ts.first('10d')
    assert len(result) == 20
    ts = tm.makeTimeDataFrame(freq='D')
    result = ts.first('10d')
    assert len(result) == 10
    result = ts.first('3M')
    expected = ts[:'3/31/2000']
    tm.assert_frame_equal(result, expected)
    result = ts.first('21D')
    expected = ts[:21]
    tm.assert_frame_equal(result, expected)
    result = ts[:0].first('3M')
    tm.assert_frame_equal(result, ts[:0])