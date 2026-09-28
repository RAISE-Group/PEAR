def test_repr(self, datetime_series, string_series, object_series):
    str(datetime_series)
    str(string_series)
    str(string_series.astype(int))
    str(object_series)
    str(Series(tm.randn(1000), index=np.arange(1000)))
    str(Series(tm.randn(1000), index=np.arange(1000, 0, step=-1)))
    str(Series(dtype=object))
    string_series[5:7] = np.NaN
    str(string_series)
    ots = datetime_series.astype('O')
    ots[::2] = None
    repr(ots)
    for name in ['', 1, 1.2, 'foo', 'αβγ', 'loooooooooooooooooooooooooooooooooooooooooooooooooooong', ('foo', 'bar', 'baz'), (1, 2), ('foo', 1, 2.3), ('α', 'β', 'γ'), ('α', 'bar')]:
        string_series.name = name
        repr(string_series)
    biggie = Series(tm.randn(1000), index=np.arange(1000), name=('foo', 'bar', 'baz'))
    repr(biggie)
    ser = Series(np.random.randn(100), name=0)
    rep_str = repr(ser)
    assert 'Name: 0' in rep_str
    ser = Series(np.random.randn(1001), name=0)
    rep_str = repr(ser)
    assert 'Name: 0' in rep_str
    ser = Series(['a\n\r\tb'], name='a\n\r\td', index=['a\n\r\tf'])
    assert '\t' not in repr(ser)
    assert '\r' not in repr(ser)
    assert 'a\n' not in repr(ser)
    s = Series([], dtype=np.int64, name='foo')
    assert repr(s) == 'Series([], Name: foo, dtype: int64)'
    s = Series([], dtype=np.int64, name=None)
    assert repr(s) == 'Series([], dtype: int64)'