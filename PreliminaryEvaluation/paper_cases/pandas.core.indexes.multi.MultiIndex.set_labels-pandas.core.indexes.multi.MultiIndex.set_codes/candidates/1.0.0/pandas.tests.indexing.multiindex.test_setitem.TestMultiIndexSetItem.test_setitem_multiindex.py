def test_setitem_multiindex(self):
    for index_fn in ('loc',):

        def assert_equal(a, b):
            assert a == b

        def check(target, indexers, value, compare_fn, expected=None):
            fn = getattr(target, index_fn)
            fn.__setitem__(indexers, value)
            result = fn.__getitem__(indexers)
            if expected is None:
                expected = value
            compare_fn(result, expected)
        index = MultiIndex.from_product([np.arange(0, 100), np.arange(0, 80)], names=['time', 'firm'])
        t, n = (0, 2)
        df = DataFrame(np.nan, columns=['A', 'w', 'l', 'a', 'x', 'X', 'd', 'profit'], index=index)
        check(target=df, indexers=((t, n), 'X'), value=0, compare_fn=assert_equal)
        df = DataFrame(-999, columns=['A', 'w', 'l', 'a', 'x', 'X', 'd', 'profit'], index=index)
        check(target=df, indexers=((t, n), 'X'), value=1, compare_fn=assert_equal)
        df = DataFrame(columns=['A', 'w', 'l', 'a', 'x', 'X', 'd', 'profit'], index=index)
        check(target=df, indexers=((t, n), 'X'), value=2, compare_fn=assert_equal)
        df = DataFrame(-999, columns=['A', 'w', 'l', 'a', 'x', 'X', 'd', 'profit'], index=index)
        check(target=df, indexers=((t, n), 'X'), value=np.array(3), compare_fn=assert_equal, expected=3)
        df = DataFrame(np.arange(25).reshape(5, 5), columns='A,B,C,D,E'.split(','), dtype=float)
        df['F'] = 99
        row_selection = df['A'] % 2 == 0
        col_selection = ['B', 'C']
        df.loc[row_selection, col_selection] = df['F']
        output = DataFrame(99.0, index=[0, 2, 4], columns=['B', 'C'])
        tm.assert_frame_equal(df.loc[row_selection, col_selection], output)
        check(target=df, indexers=(row_selection, col_selection), value=df['F'], compare_fn=tm.assert_frame_equal, expected=output)
        idx = MultiIndex.from_product([['A', 'B', 'C'], date_range('2015-01-01', '2015-04-01', freq='MS')])
        cols = MultiIndex.from_product([['foo', 'bar'], date_range('2016-01-01', '2016-02-01', freq='MS')])
        df = DataFrame(np.random.random((12, 4)), index=idx, columns=cols)
        subidx = MultiIndex.from_tuples([('A', Timestamp('2015-01-01')), ('A', Timestamp('2015-02-01'))])
        subcols = MultiIndex.from_tuples([('foo', Timestamp('2016-01-01')), ('foo', Timestamp('2016-02-01'))])
        vals = DataFrame(np.random.random((2, 2)), index=subidx, columns=subcols)
        check(target=df, indexers=(subidx, subcols), value=vals, compare_fn=tm.assert_frame_equal)
        vals = DataFrame(np.random.random((2, 4)), index=subidx, columns=cols)
        check(target=df, indexers=(subidx, slice(None, None, None)), value=vals, compare_fn=tm.assert_frame_equal)
        copy = df.copy()
        check(target=df, indexers=(df.index, df.columns), value=df, compare_fn=tm.assert_frame_equal, expected=copy)