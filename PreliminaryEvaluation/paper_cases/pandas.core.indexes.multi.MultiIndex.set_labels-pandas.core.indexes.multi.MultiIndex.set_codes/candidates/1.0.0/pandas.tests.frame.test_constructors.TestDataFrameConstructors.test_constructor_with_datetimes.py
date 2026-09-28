def test_constructor_with_datetimes(self):
    intname = np.dtype(np.int_).name
    floatname = np.dtype(np.float_).name
    datetime64name = np.dtype('M8[ns]').name
    objectname = np.dtype(np.object_).name
    df = DataFrame({'A': 1, 'B': 'foo', 'C': 'bar', 'D': Timestamp('20010101'), 'E': datetime(2001, 1, 2, 0, 0)}, index=np.arange(10))
    result = df.dtypes
    expected = Series([np.dtype('int64')] + [np.dtype(objectname)] * 2 + [np.dtype(datetime64name)] * 2, index=list('ABCDE'))
    tm.assert_series_equal(result, expected)
    df = DataFrame({'a': 1.0, 'b': 2, 'c': 'foo', floatname: np.array(1.0, dtype=floatname), intname: np.array(1, dtype=intname)}, index=np.arange(10))
    result = df.dtypes
    expected = Series([np.dtype('float64')] + [np.dtype('int64')] + [np.dtype('object')] + [np.dtype('float64')] + [np.dtype(intname)], index=['a', 'b', 'c', floatname, intname])
    tm.assert_series_equal(result, expected)
    df = DataFrame({'a': 1.0, 'b': 2, 'c': 'foo', floatname: np.array([1.0] * 10, dtype=floatname), intname: np.array([1] * 10, dtype=intname)}, index=np.arange(10))
    result = df.dtypes
    expected = Series([np.dtype('float64')] + [np.dtype('int64')] + [np.dtype('object')] + [np.dtype('float64')] + [np.dtype(intname)], index=['a', 'b', 'c', floatname, intname])
    tm.assert_series_equal(result, expected)
    ind = date_range(start='2000-01-01', freq='D', periods=10)
    datetimes = [ts.to_pydatetime() for ts in ind]
    datetime_s = Series(datetimes)
    assert datetime_s.dtype == 'M8[ns]'
    ind = date_range(start='2000-01-01', freq='D', periods=10)
    datetimes = [ts.to_pydatetime() for ts in ind]
    dates = [ts.date() for ts in ind]
    df = DataFrame(datetimes, columns=['datetimes'])
    df['dates'] = dates
    result = df.dtypes
    expected = Series([np.dtype('datetime64[ns]'), np.dtype('object')], index=['datetimes', 'dates'])
    tm.assert_series_equal(result, expected)
    import pytz
    tz = pytz.timezone('US/Eastern')
    dt = tz.localize(datetime(2012, 1, 1))
    df = DataFrame({'End Date': dt}, index=[0])
    assert df.iat[0, 0] == dt
    tm.assert_series_equal(df.dtypes, Series({'End Date': 'datetime64[ns, US/Eastern]'}))
    df = DataFrame([{'End Date': dt}])
    assert df.iat[0, 0] == dt
    tm.assert_series_equal(df.dtypes, Series({'End Date': 'datetime64[ns, US/Eastern]'}))
    dr = date_range('20130101', periods=3)
    df = DataFrame({'value': dr})
    assert df.iat[0, 0].tz is None
    dr = date_range('20130101', periods=3, tz='UTC')
    df = DataFrame({'value': dr})
    assert str(df.iat[0, 0].tz) == 'UTC'
    dr = date_range('20130101', periods=3, tz='US/Eastern')
    df = DataFrame({'value': dr})
    assert str(df.iat[0, 0].tz) == 'US/Eastern'
    i = date_range('1/1/2011', periods=5, freq='10s', tz='US/Eastern')
    expected = DataFrame({'a': i.to_series().reset_index(drop=True)})
    df = DataFrame()
    df['a'] = i
    tm.assert_frame_equal(df, expected)
    df = DataFrame({'a': i})
    tm.assert_frame_equal(df, expected)
    i_no_tz = date_range('1/1/2011', periods=5, freq='10s')
    df = DataFrame({'a': i, 'b': i_no_tz})
    expected = DataFrame({'a': i.to_series().reset_index(drop=True), 'b': i_no_tz})
    tm.assert_frame_equal(df, expected)