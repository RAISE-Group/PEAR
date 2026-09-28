def test_dt_accessor_api_for_categorical(self):
    from pandas.core.indexes.accessors import Properties
    s_dr = Series(date_range('1/1/2015', periods=5, tz='MET'))
    c_dr = s_dr.astype('category')
    s_pr = Series(period_range('1/1/2015', freq='D', periods=5))
    c_pr = s_pr.astype('category')
    s_tdr = Series(timedelta_range('1 days', '10 days'))
    c_tdr = s_tdr.astype('category')
    get_ops = lambda x: x._datetimelike_ops
    test_data = [('Datetime', get_ops(DatetimeIndex), s_dr, c_dr), ('Period', get_ops(PeriodArray), s_pr, c_pr), ('Timedelta', get_ops(TimedeltaIndex), s_tdr, c_tdr)]
    assert isinstance(c_dr.dt, Properties)
    special_func_defs = [('strftime', ('%Y-%m-%d',), {}), ('tz_convert', ('EST',), {}), ('round', ('D',), {}), ('floor', ('D',), {}), ('ceil', ('D',), {}), ('asfreq', ('D',), {})]
    _special_func_names = [f[0] for f in special_func_defs]
    _ignore_names = ['tz_localize', 'components']
    for name, attr_names, s, c in test_data:
        func_names = [f for f in dir(s.dt) if not (f.startswith('_') or f in attr_names or f in _special_func_names or (f in _ignore_names))]
        func_defs = [(f, (), {}) for f in func_names]
        for f_def in special_func_defs:
            if f_def[0] in dir(s.dt):
                func_defs.append(f_def)
        for func, args, kwargs in func_defs:
            with warnings.catch_warnings():
                if func == 'to_period':
                    warnings.simplefilter('ignore', UserWarning)
                res = getattr(c.dt, func)(*args, **kwargs)
                exp = getattr(s.dt, func)(*args, **kwargs)
            tm.assert_equal(res, exp)
        for attr in attr_names:
            res = getattr(c.dt, attr)
            exp = getattr(s.dt, attr)
        if isinstance(res, DataFrame):
            tm.assert_frame_equal(res, exp)
        elif isinstance(res, Series):
            tm.assert_series_equal(res, exp)
        else:
            tm.assert_almost_equal(res, exp)
    invalid = Series([1, 2, 3]).astype('category')
    msg = 'Can only use .dt accessor with datetimelike'
    with pytest.raises(AttributeError, match=msg):
        invalid.dt
    assert not hasattr(invalid, 'str')