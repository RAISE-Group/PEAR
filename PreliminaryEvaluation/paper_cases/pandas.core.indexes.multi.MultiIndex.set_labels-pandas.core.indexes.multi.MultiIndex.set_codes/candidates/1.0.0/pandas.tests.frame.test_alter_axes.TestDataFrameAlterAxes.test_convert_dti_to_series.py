def test_convert_dti_to_series(self):
    idx = DatetimeIndex(to_datetime(['2013-1-1 13:00', '2013-1-2 14:00']), name='B').tz_localize('US/Pacific')
    df = DataFrame(np.random.randn(2, 1), columns=['A'])
    expected = Series(np.array([Timestamp('2013-01-01 13:00:00-0800', tz='US/Pacific'), Timestamp('2013-01-02 14:00:00-0800', tz='US/Pacific')], dtype='object'), name='B')
    result = Series(idx)
    tm.assert_series_equal(result, expected)
    df['B'] = idx
    result = df['B']
    tm.assert_series_equal(result, expected)
    msg = "stop passing 'keep_tz'"
    with tm.assert_produces_warning(FutureWarning) as m:
        result = idx.to_series(keep_tz=True, index=[0, 1])
    tm.assert_series_equal(result, expected)
    assert msg in str(m[0].message)
    with tm.assert_produces_warning(FutureWarning) as m:
        df['B'] = idx.to_series(keep_tz=False, index=[0, 1])
    result = df['B']
    comp = Series(DatetimeIndex(expected.values).tz_localize(None), name='B')
    tm.assert_series_equal(result, comp)
    msg = "do 'idx.tz_convert(None)' before calling"
    assert msg in str(m[0].message)
    result = idx.to_series(index=[0, 1])
    tm.assert_series_equal(result, expected)
    with tm.assert_produces_warning(FutureWarning) as m:
        result = idx.to_series(keep_tz=False, index=[0, 1])
    tm.assert_series_equal(result, expected.dt.tz_convert(None))
    msg = "do 'idx.tz_convert(None)' before calling"
    assert msg in str(m[0].message)
    df['B'] = idx.to_pydatetime()
    result = df['B']
    tm.assert_series_equal(result, expected)
    import pytz
    df = DataFrame([{'ts': datetime(2014, 4, 1, tzinfo=pytz.utc), 'foo': 1}])
    expected = df.set_index('ts')
    df.index = df['ts']
    df.pop('ts')
    tm.assert_frame_equal(df, expected)