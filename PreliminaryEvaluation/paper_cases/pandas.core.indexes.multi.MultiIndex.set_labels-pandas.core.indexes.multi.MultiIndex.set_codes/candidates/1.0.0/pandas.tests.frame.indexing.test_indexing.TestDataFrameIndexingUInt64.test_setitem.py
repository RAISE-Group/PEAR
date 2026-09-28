def test_setitem(self, uint64_frame):
    df = uint64_frame
    idx = df['A'].rename('foo')
    df['C'] = idx
    tm.assert_series_equal(df['C'], Series(idx, name='C'))
    df['D'] = 'foo'
    df['D'] = idx
    tm.assert_series_equal(df['D'], Series(idx, name='D'))
    del df['D']
    df2 = df.copy()
    df2.iloc[1, 1] = pd.NaT
    df2.iloc[1, 2] = pd.NaT
    result = df2['B']
    tm.assert_series_equal(notna(result), Series([True, False, True], name='B'))
    tm.assert_series_equal(df2.dtypes, Series([np.dtype('uint64'), np.dtype('O'), np.dtype('O')], index=['A', 'B', 'C']))