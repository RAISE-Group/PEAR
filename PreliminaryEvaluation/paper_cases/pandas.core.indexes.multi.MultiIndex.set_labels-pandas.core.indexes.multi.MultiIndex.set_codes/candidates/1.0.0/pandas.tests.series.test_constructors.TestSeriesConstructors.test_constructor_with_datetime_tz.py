def test_constructor_with_datetime_tz(self):
    dr = date_range('20130101', periods=3, tz='US/Eastern')
    s = Series(dr)
    assert s.dtype.name == 'datetime64[ns, US/Eastern]'
    assert s.dtype == 'datetime64[ns, US/Eastern]'
    assert is_datetime64tz_dtype(s.dtype)
    assert 'datetime64[ns, US/Eastern]' in str(s)
    result = s.values
    assert isinstance(result, np.ndarray)
    assert result.dtype == 'datetime64[ns]'
    exp = pd.DatetimeIndex(result)
    exp = exp.tz_localize('UTC').tz_convert(tz=s.dt.tz)
    tm.assert_index_equal(dr, exp)
    result = s.iloc[0]
    assert result == Timestamp('2013-01-01 00:00:00-0500', tz='US/Eastern', freq='D')
    result = s[0]
    assert result == Timestamp('2013-01-01 00:00:00-0500', tz='US/Eastern', freq='D')
    result = s[Series([True, True, False], index=s.index)]
    tm.assert_series_equal(result, s[0:2])
    result = s.iloc[0:1]
    tm.assert_series_equal(result, Series(dr[0:1]))
    result = pd.concat([s.iloc[0:1], s.iloc[1:]])
    tm.assert_series_equal(result, s)
    assert 'datetime64[ns, US/Eastern]' in str(s)
    result = s.shift()
    assert 'datetime64[ns, US/Eastern]' in str(result)
    assert 'NaT' in str(result)
    t = Series(date_range('20130101', periods=1000, tz='US/Eastern'))
    assert 'datetime64[ns, US/Eastern]' in str(t)
    result = pd.DatetimeIndex(s, freq='infer')
    tm.assert_index_equal(result, dr)
    s = Series([pd.Timestamp('2013-01-01 13:00:00-0800', tz='US/Pacific'), pd.Timestamp('2013-01-02 14:00:00-0800', tz='US/Pacific')])
    assert s.dtype == 'datetime64[ns, US/Pacific]'
    assert lib.infer_dtype(s, skipna=True) == 'datetime64'
    s = Series([pd.Timestamp('2013-01-01 13:00:00-0800', tz='US/Pacific'), pd.Timestamp('2013-01-02 14:00:00-0800', tz='US/Eastern')])
    assert s.dtype == 'object'
    assert lib.infer_dtype(s, skipna=True) == 'datetime'
    s = Series(pd.NaT, index=[0, 1], dtype='datetime64[ns, US/Eastern]')
    expected = Series(pd.DatetimeIndex(['NaT', 'NaT'], tz='US/Eastern'))
    tm.assert_series_equal(s, expected)