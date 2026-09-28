def test_timedelta(self):
    converter = lambda x: pd.to_timedelta(x, unit='ms')
    s = Series([timedelta(23), timedelta(seconds=5)])
    assert s.dtype == 'timedelta64[ns]'
    result = pd.read_json(s.to_json(), typ='series').apply(converter)
    tm.assert_series_equal(result, s)
    s = Series([timedelta(23), timedelta(seconds=5)], index=pd.Index([0, 1]))
    assert s.dtype == 'timedelta64[ns]'
    result = pd.read_json(s.to_json(), typ='series').apply(converter)
    tm.assert_series_equal(result, s)
    frame = DataFrame([timedelta(23), timedelta(seconds=5)])
    assert frame[0].dtype == 'timedelta64[ns]'
    tm.assert_frame_equal(frame, pd.read_json(frame.to_json()).apply(converter))
    frame = DataFrame({'a': [timedelta(days=23), timedelta(seconds=5)], 'b': [1, 2], 'c': pd.date_range(start='20130101', periods=2)})
    result = pd.read_json(frame.to_json(date_unit='ns'))
    result['a'] = pd.to_timedelta(result.a, unit='ns')
    result['c'] = pd.to_datetime(result.c)
    tm.assert_frame_equal(frame, result)