def test_last_subset(self):
    ts = tm.makeTimeDataFrame(freq='12h')
    result = ts.last('10d')
    assert len(result) == 20
    ts = tm.makeTimeDataFrame(nper=30, freq='D')
    result = ts.last('10d')
    assert len(result) == 10
    result = ts.last('21D')
    expected = ts['2000-01-10':]
    tm.assert_frame_equal(result, expected)
    result = ts.last('21D')
    expected = ts[-21:]
    tm.assert_frame_equal(result, expected)
    result = ts[:0].last('3M')
    tm.assert_frame_equal(result, ts[:0])