def test_stack_partial_multiIndex(self):

    def _test_stack_with_multiindex(multiindex):
        df = DataFrame(np.arange(3 * len(multiindex)).reshape(3, len(multiindex)), columns=multiindex)
        for level in (-1, 0, 1, [0, 1], [1, 0]):
            result = df.stack(level=level, dropna=False)
            if isinstance(level, int):
                expected = df.stack(level=level, dropna=True)
                if isinstance(expected, Series):
                    tm.assert_series_equal(result, expected)
                else:
                    tm.assert_frame_equal(result, expected)
            df.columns = MultiIndex.from_tuples(df.columns.to_numpy(), names=df.columns.names)
            expected = df.stack(level=level, dropna=False)
            if isinstance(expected, Series):
                tm.assert_series_equal(result, expected)
            else:
                tm.assert_frame_equal(result, expected)
    full_multiindex = MultiIndex.from_tuples([('B', 'x'), ('B', 'z'), ('A', 'y'), ('C', 'x'), ('C', 'u')], names=['Upper', 'Lower'])
    for multiindex_columns in ([0, 1, 2, 3, 4], [0, 1, 2, 3], [0, 1, 2, 4], [0, 1, 2], [1, 2, 3], [2, 3, 4], [0, 1], [0, 2], [0, 3], [0], [2], [4]):
        _test_stack_with_multiindex(full_multiindex[multiindex_columns])
        if len(multiindex_columns) > 1:
            multiindex_columns.reverse()
            _test_stack_with_multiindex(full_multiindex[multiindex_columns])
    df = DataFrame(np.arange(6).reshape(2, 3), columns=full_multiindex[[0, 1, 3]])
    result = df.stack(dropna=False)
    expected = DataFrame([[0, 2], [1, np.nan], [3, 5], [4, np.nan]], index=MultiIndex(levels=[[0, 1], ['u', 'x', 'y', 'z']], codes=[[0, 0, 1, 1], [1, 3, 1, 3]], names=[None, 'Lower']), columns=Index(['B', 'C'], name='Upper'), dtype=df.dtypes[0])
    tm.assert_frame_equal(result, expected)