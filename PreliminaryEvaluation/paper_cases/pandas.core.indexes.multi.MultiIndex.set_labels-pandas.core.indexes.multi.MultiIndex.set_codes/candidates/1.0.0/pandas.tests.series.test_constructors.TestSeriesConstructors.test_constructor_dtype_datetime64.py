def test_constructor_dtype_datetime64(self):
    s = Series(iNaT, dtype='M8[ns]', index=range(5))
    assert isna(s).all()
    s = Series(iNaT, index=range(5))
    assert not isna(s).all()
    s = Series(np.nan, dtype='M8[ns]', index=range(5))
    assert isna(s).all()
    s = Series([datetime(2001, 1, 2, 0, 0), iNaT], dtype='M8[ns]')
    assert isna(s[1])
    assert s.dtype == 'M8[ns]'
    s = Series([datetime(2001, 1, 2, 0, 0), np.nan], dtype='M8[ns]')
    assert isna(s[1])
    assert s.dtype == 'M8[ns]'
    dates = [np.datetime64(datetime(2013, 1, 1)), np.datetime64(datetime(2013, 1, 2)), np.datetime64(datetime(2013, 1, 3))]
    s = Series(dates)
    assert s.dtype == 'M8[ns]'
    s.iloc[0] = np.nan
    assert s.dtype == 'M8[ns]'
    expected = Series([datetime(2013, 1, 1), datetime(2013, 1, 2), datetime(2013, 1, 3)], dtype='datetime64[ns]')
    result = Series(Series(dates).astype(np.int64) / 1000000, dtype='M8[ms]')
    tm.assert_series_equal(result, expected)
    result = Series(dates, dtype='datetime64[ns]')
    tm.assert_series_equal(result, expected)
    expected = Series([pd.NaT, datetime(2013, 1, 2), datetime(2013, 1, 3)], dtype='datetime64[ns]')
    result = Series([np.nan] + dates[1:], dtype='datetime64[ns]')
    tm.assert_series_equal(result, expected)
    dts = Series(dates, dtype='datetime64[ns]')
    dts.astype('int64')
    msg = 'cannot astype a datetimelike from \\[datetime64\\[ns\\]\\] to \\[int32\\]'
    with pytest.raises(TypeError, match=msg):
        dts.astype('int32')
    result = Series(dts, dtype=np.int64)
    expected = Series(dts.astype(np.int64))
    tm.assert_series_equal(result, expected)
    result = Series([datetime(2, 1, 1)])
    assert result[0] == datetime(2, 1, 1, 0, 0)
    result = Series([datetime(3000, 1, 1)])
    assert result[0] == datetime(3000, 1, 1, 0, 0)
    result = Series([Timestamp('20130101'), 1], index=['a', 'b'])
    assert result['a'] == Timestamp('20130101')
    assert result['b'] == 1
    dates = date_range('01-Jan-2015', '01-Dec-2015', freq='M')
    values2 = dates.view(np.ndarray).astype('datetime64[ns]')
    expected = Series(values2, index=dates)
    for dtype in ['s', 'D', 'ms', 'us', 'ns']:
        values1 = dates.view(np.ndarray).astype('M8[{0}]'.format(dtype))
        result = Series(values1, dates)
        tm.assert_series_equal(result, expected)
    expected = Series(values2, index=dates, dtype=object)
    for dtype in ['s', 'D', 'ms', 'us', 'ns']:
        values1 = dates.view(np.ndarray).astype('M8[{0}]'.format(dtype))
        result = Series(values1, index=dates, dtype=object)
        tm.assert_series_equal(result, expected)
    dates2 = np.array([d.date() for d in dates.to_pydatetime()], dtype=object)
    series1 = Series(dates2, dates)
    tm.assert_numpy_array_equal(series1.values, dates2)
    assert series1.dtype == object
    s = Series([None, pd.NaT, '2013-08-05 15:30:00.000001'])
    assert s.dtype == 'datetime64[ns]'
    s = Series([np.nan, pd.NaT, '2013-08-05 15:30:00.000001'])
    assert s.dtype == 'datetime64[ns]'
    s = Series([pd.NaT, None, '2013-08-05 15:30:00.000001'])
    assert s.dtype == 'datetime64[ns]'
    s = Series([pd.NaT, np.nan, '2013-08-05 15:30:00.000001'])
    assert s.dtype == 'datetime64[ns]'
    dr = date_range('20130101', periods=3)
    assert Series(dr).iloc[0].tz is None
    dr = date_range('20130101', periods=3, tz='UTC')
    assert str(Series(dr).iloc[0].tz) == 'UTC'
    dr = date_range('20130101', periods=3, tz='US/Eastern')
    assert str(Series(dr).iloc[0].tz) == 'US/Eastern'
    s = Series([1479596223000, -1479590, pd.NaT])
    assert s.dtype == 'object'
    assert s[2] is pd.NaT
    assert 'NaT' in str(s)
    s = Series([datetime(2010, 1, 1), datetime(2, 1, 1), pd.NaT])
    assert s.dtype == 'object'
    assert s[2] is pd.NaT
    assert 'NaT' in str(s)
    s = Series([datetime(2010, 1, 1), datetime(2, 1, 1), np.nan])
    assert s.dtype == 'object'
    assert s[2] is np.nan
    assert 'NaN' in str(s)