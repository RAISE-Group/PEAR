def test_setitem_single_column_mixed_datetime(self):
    df = DataFrame(np.random.randn(5, 3), index=['a', 'b', 'c', 'd', 'e'], columns=['foo', 'bar', 'baz'])
    df['timestamp'] = Timestamp('20010102')
    result = df.dtypes
    expected = Series([np.dtype('float64')] * 3 + [np.dtype('datetime64[ns]')], index=['foo', 'bar', 'baz', 'timestamp'])
    tm.assert_series_equal(result, expected)
    df.loc['b', 'timestamp'] = iNaT
    assert not isna(df.loc['b', 'timestamp'])
    assert df['timestamp'].dtype == np.object_
    assert df.loc['b', 'timestamp'] == iNaT
    df.loc['c', 'timestamp'] = np.nan
    assert isna(df.loc['c', 'timestamp'])
    df.loc['d', :] = np.nan
    assert not isna(df.loc['c', :]).all()