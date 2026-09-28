def test_dt_namespace_accessor(self):
    ok_for_period = PeriodArray._datetimelike_ops
    ok_for_period_methods = ['strftime', 'to_timestamp', 'asfreq']
    ok_for_dt = DatetimeIndex._datetimelike_ops
    ok_for_dt_methods = ['to_period', 'to_pydatetime', 'tz_localize', 'tz_convert', 'normalize', 'strftime', 'round', 'floor', 'ceil', 'day_name', 'month_name']
    ok_for_td = TimedeltaIndex._datetimelike_ops
    ok_for_td_methods = ['components', 'to_pytimedelta', 'total_seconds', 'round', 'floor', 'ceil']

    def get_expected(s, name):
        result = getattr(Index(s._values), prop)
        if isinstance(result, np.ndarray):
            if is_integer_dtype(result):
                result = result.astype('int64')
        elif not is_list_like(result):
            return result
        return Series(result, index=s.index, name=s.name)

    def compare(s, name):
        a = getattr(s.dt, prop)
        b = get_expected(s, prop)
        if not (is_list_like(a) and is_list_like(b)):
            assert a == b
        else:
            tm.assert_series_equal(a, b)
    cases = [Series(date_range('20130101', periods=5), name='xxx'), Series(date_range('20130101', periods=5, freq='s'), name='xxx'), Series(date_range('20130101 00:00:00', periods=5, freq='ms'), name='xxx')]
    for s in cases:
        for prop in ok_for_dt:
            if prop != 'freq':
                compare(s, prop)
        for prop in ok_for_dt_methods:
            getattr(s.dt, prop)
        result = s.dt.to_pydatetime()
        assert isinstance(result, np.ndarray)
        assert result.dtype == object
        result = s.dt.tz_localize('US/Eastern')
        exp_values = DatetimeIndex(s.values).tz_localize('US/Eastern')
        expected = Series(exp_values, index=s.index, name='xxx')
        tm.assert_series_equal(result, expected)
        tz_result = result.dt.tz
        assert str(tz_result) == 'US/Eastern'
        freq_result = s.dt.freq
        assert freq_result == DatetimeIndex(s.values, freq='infer').freq
        result = s.dt.tz_localize('UTC').dt.tz_convert('US/Eastern')
        exp_values = DatetimeIndex(s.values).tz_localize('UTC').tz_convert('US/Eastern')
        expected = Series(exp_values, index=s.index, name='xxx')
        tm.assert_series_equal(result, expected)
    s = Series(date_range('20130101', periods=5, tz='US/Eastern'), name='xxx')
    for prop in ok_for_dt:
        if prop != 'freq':
            compare(s, prop)
    for prop in ok_for_dt_methods:
        getattr(s.dt, prop)
    result = s.dt.to_pydatetime()
    assert isinstance(result, np.ndarray)
    assert result.dtype == object
    result = s.dt.tz_convert('CET')
    expected = Series(s._values.tz_convert('CET'), index=s.index, name='xxx')
    tm.assert_series_equal(result, expected)
    tz_result = result.dt.tz
    assert str(tz_result) == 'CET'
    freq_result = s.dt.freq
    assert freq_result == DatetimeIndex(s.values, freq='infer').freq
    cases = [Series(timedelta_range('1 day', periods=5), index=list('abcde'), name='xxx'), Series(timedelta_range('1 day 01:23:45', periods=5, freq='s'), name='xxx'), Series(timedelta_range('2 days 01:23:45.012345', periods=5, freq='ms'), name='xxx')]
    for s in cases:
        for prop in ok_for_td:
            if prop != 'freq':
                compare(s, prop)
        for prop in ok_for_td_methods:
            getattr(s.dt, prop)
        result = s.dt.components
        assert isinstance(result, DataFrame)
        tm.assert_index_equal(result.index, s.index)
        result = s.dt.to_pytimedelta()
        assert isinstance(result, np.ndarray)
        assert result.dtype == object
        result = s.dt.total_seconds()
        assert isinstance(result, pd.Series)
        assert result.dtype == 'float64'
        freq_result = s.dt.freq
        assert freq_result == TimedeltaIndex(s.values, freq='infer').freq
    index = date_range('20130101', periods=3, freq='D')
    s = Series(date_range('20140204', periods=3, freq='s'), index=index, name='xxx')
    exp = Series(np.array([2014, 2014, 2014], dtype='int64'), index=index, name='xxx')
    tm.assert_series_equal(s.dt.year, exp)
    exp = Series(np.array([2, 2, 2], dtype='int64'), index=index, name='xxx')
    tm.assert_series_equal(s.dt.month, exp)
    exp = Series(np.array([0, 1, 2], dtype='int64'), index=index, name='xxx')
    tm.assert_series_equal(s.dt.second, exp)
    exp = pd.Series([s[0]] * 3, index=index, name='xxx')
    tm.assert_series_equal(s.dt.normalize(), exp)
    cases = [Series(period_range('20130101', periods=5, freq='D'), name='xxx')]
    for s in cases:
        for prop in ok_for_period:
            if prop != 'freq':
                compare(s, prop)
        for prop in ok_for_period_methods:
            getattr(s.dt, prop)
        freq_result = s.dt.freq
        assert freq_result == PeriodIndex(s.values).freq

    def get_dir(s):
        results = [r for r in s.dt.__dir__() if not r.startswith('_')]
        return sorted(set(results))
    s = Series(date_range('20130101', periods=5, freq='D'), name='xxx')
    results = get_dir(s)
    tm.assert_almost_equal(results, sorted(set(ok_for_dt + ok_for_dt_methods)))
    s = Series(period_range('20130101', periods=5, freq='D', name='xxx').astype(object))
    results = get_dir(s)
    tm.assert_almost_equal(results, sorted(set(ok_for_period + ok_for_period_methods)))
    s = Series(pd.date_range('2015-01-01', '2016-01-01', freq='T'), name='xxx')
    s = s.dt.tz_localize('UTC').dt.tz_convert('America/Chicago')
    results = get_dir(s)
    tm.assert_almost_equal(results, sorted(set(ok_for_dt + ok_for_dt_methods)))
    exp_values = pd.date_range('2015-01-01', '2016-01-01', freq='T', tz='UTC').tz_convert('America/Chicago')
    expected = Series(exp_values, name='xxx')
    tm.assert_series_equal(s, expected)
    s = Series(date_range('20130101', periods=5, freq='D'), name='xxx')
    with pytest.raises(ValueError, match='modifications'):
        s.dt.hour = 5
    with pd.option_context('chained_assignment', 'raise'):
        with pytest.raises(com.SettingWithCopyError):
            s.dt.hour[0] = 5