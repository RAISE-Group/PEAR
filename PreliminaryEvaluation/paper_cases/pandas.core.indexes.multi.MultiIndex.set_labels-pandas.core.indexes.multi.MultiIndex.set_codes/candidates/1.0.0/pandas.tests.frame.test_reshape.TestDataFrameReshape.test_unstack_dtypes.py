def test_unstack_dtypes(self):
    rows = [[1, 1, 3, 4], [1, 2, 3, 4], [2, 1, 3, 4], [2, 2, 3, 4]]
    df = DataFrame(rows, columns=list('ABCD'))
    result = df.dtypes
    expected = Series([np.dtype('int64')] * 4, index=list('ABCD'))
    tm.assert_series_equal(result, expected)
    df2 = df.set_index(['A', 'B'])
    df3 = df2.unstack('B')
    result = df3.dtypes
    expected = Series([np.dtype('int64')] * 4, index=pd.MultiIndex.from_arrays([['C', 'C', 'D', 'D'], [1, 2, 1, 2]], names=(None, 'B')))
    tm.assert_series_equal(result, expected)
    df2 = df.set_index(['A', 'B'])
    df2['C'] = 3.0
    df3 = df2.unstack('B')
    result = df3.dtypes
    expected = Series([np.dtype('float64')] * 2 + [np.dtype('int64')] * 2, index=pd.MultiIndex.from_arrays([['C', 'C', 'D', 'D'], [1, 2, 1, 2]], names=(None, 'B')))
    tm.assert_series_equal(result, expected)
    df2['D'] = 'foo'
    df3 = df2.unstack('B')
    result = df3.dtypes
    expected = Series([np.dtype('float64')] * 2 + [np.dtype('object')] * 2, index=pd.MultiIndex.from_arrays([['C', 'C', 'D', 'D'], [1, 2, 1, 2]], names=(None, 'B')))
    tm.assert_series_equal(result, expected)
    for c, d in ((np.zeros(5), np.zeros(5)), (np.arange(5, dtype='f8'), np.arange(5, 10, dtype='f8'))):
        df = DataFrame({'A': ['a'] * 5, 'C': c, 'D': d, 'B': pd.date_range('2012-01-01', periods=5)})
        right = df.iloc[:3].copy(deep=True)
        df = df.set_index(['A', 'B'])
        df['D'] = df['D'].astype('int64')
        left = df.iloc[:3].unstack(0)
        right = right.set_index(['A', 'B']).unstack(0)
        right['D', 'a'] = right['D', 'a'].astype('int64')
        assert left.shape == (3, 2)
        tm.assert_frame_equal(left, right)