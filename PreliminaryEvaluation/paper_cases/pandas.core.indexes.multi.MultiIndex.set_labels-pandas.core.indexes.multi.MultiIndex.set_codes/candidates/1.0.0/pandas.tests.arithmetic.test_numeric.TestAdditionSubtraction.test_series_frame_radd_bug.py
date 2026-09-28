def test_series_frame_radd_bug(self):
    vals = pd.Series(tm.rands_array(5, 10))
    result = 'foo_' + vals
    expected = vals.map(lambda x: 'foo_' + x)
    tm.assert_series_equal(result, expected)
    frame = pd.DataFrame({'vals': vals})
    result = 'foo_' + frame
    expected = pd.DataFrame({'vals': vals.map(lambda x: 'foo_' + x)})
    tm.assert_frame_equal(result, expected)
    ts = tm.makeTimeSeries()
    ts.name = 'ts'
    now = pd.Timestamp.now().to_pydatetime()
    with pytest.raises(TypeError):
        now + ts
    with pytest.raises(TypeError):
        ts + now