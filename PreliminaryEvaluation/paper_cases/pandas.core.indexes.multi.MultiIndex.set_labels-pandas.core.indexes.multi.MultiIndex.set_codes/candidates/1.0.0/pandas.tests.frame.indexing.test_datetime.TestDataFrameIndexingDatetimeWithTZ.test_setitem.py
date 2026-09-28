def test_setitem(self, timezone_frame):
    df = timezone_frame
    idx = df['B'].rename('foo')
    df['C'] = idx
    tm.assert_series_equal(df['C'], Series(idx, name='C'))
    df['D'] = 'foo'
    df['D'] = idx
    tm.assert_series_equal(df['D'], Series(idx, name='D'))
    del df['D']
    b1 = df._data.blocks[1]
    b2 = df._data.blocks[2]
    tm.assert_extension_array_equal(b1.values, b2.values)
    assert id(b1.values._data.base) != id(b2.values._data.base)
    df2 = df.copy()
    df2.iloc[1, 1] = pd.NaT
    df2.iloc[1, 2] = pd.NaT
    result = df2['B']
    tm.assert_series_equal(notna(result), Series([True, False, True], name='B'))
    tm.assert_series_equal(df2.dtypes, df.dtypes)