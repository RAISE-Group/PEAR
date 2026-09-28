def test_constructor_dtype_timedelta64(self):
    td = Series([timedelta(days=i) for i in range(3)])
    assert td.dtype == 'timedelta64[ns]'
    td = Series([timedelta(days=1)])
    assert td.dtype == 'timedelta64[ns]'
    td = Series([timedelta(days=1), timedelta(days=2), np.timedelta64(1, 's')])
    assert td.dtype == 'timedelta64[ns]'
    td = Series([timedelta(days=1), NaT], dtype='m8[ns]')
    assert td.dtype == 'timedelta64[ns]'
    td = Series([timedelta(days=1), np.nan], dtype='m8[ns]')
    assert td.dtype == 'timedelta64[ns]'
    td = Series([np.timedelta64(300000000), pd.NaT], dtype='m8[ns]')
    assert td.dtype == 'timedelta64[ns]'
    td = Series([np.timedelta64(300000000), NaT])
    assert td.dtype == 'timedelta64[ns]'
    td = Series([np.timedelta64(300000000), iNaT])
    assert td.dtype == 'object'
    td = Series([np.timedelta64(300000000), np.nan])
    assert td.dtype == 'timedelta64[ns]'
    td = Series([pd.NaT, np.timedelta64(300000000)])
    assert td.dtype == 'timedelta64[ns]'
    td = Series([np.timedelta64(1, 's')])
    assert td.dtype == 'timedelta64[ns]'
    td.astype('int64')
    msg = 'cannot astype a timedelta from \\[timedelta64\\[ns\\]\\] to \\[int32\\]'
    with pytest.raises(TypeError, match=msg):
        td.astype('int32')
    msg = 'Could not convert object to NumPy timedelta'
    with pytest.raises(ValueError, match=msg):
        Series([timedelta(days=1), 'foo'], dtype='m8[ns]')
    td = Series([timedelta(days=i) for i in range(3)] + ['foo'])
    assert td.dtype == 'object'
    s = Series([None, pd.NaT, '1 Day'])
    assert s.dtype == 'timedelta64[ns]'
    s = Series([np.nan, pd.NaT, '1 Day'])
    assert s.dtype == 'timedelta64[ns]'
    s = Series([pd.NaT, None, '1 Day'])
    assert s.dtype == 'timedelta64[ns]'
    s = Series([pd.NaT, np.nan, '1 Day'])
    assert s.dtype == 'timedelta64[ns]'