def test_nanosecond_index_access(self):
    s = Series([Timestamp('20130101')]).values.view('i8')[0]
    r = DatetimeIndex([s + 50 + i for i in range(100)])
    x = Series(np.random.randn(100), index=r)
    first_value = x.asof(x.index[0])
    expected_ts = np_datetime64_compat('2013-01-01 00:00:00.000000050+0000', 'ns')
    assert first_value == x[Timestamp(expected_ts)]