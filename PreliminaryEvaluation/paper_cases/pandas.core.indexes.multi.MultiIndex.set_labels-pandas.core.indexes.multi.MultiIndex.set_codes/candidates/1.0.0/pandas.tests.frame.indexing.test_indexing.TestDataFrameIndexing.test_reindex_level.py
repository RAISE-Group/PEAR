def test_reindex_level(self):
    from itertools import permutations
    icol = ['jim', 'joe', 'jolie']

    def verify_first_level(df, level, idx, check_index_type=True):

        def f(val):
            return np.nonzero((df[level] == val).to_numpy())[0]
        i = np.concatenate(list(map(f, idx)))
        left = df.set_index(icol).reindex(idx, level=level)
        right = df.iloc[i].set_index(icol)
        tm.assert_frame_equal(left, right, check_index_type=check_index_type)

    def verify(df, level, idx, indexer, check_index_type=True):
        left = df.set_index(icol).reindex(idx, level=level)
        right = df.iloc[indexer].set_index(icol)
        tm.assert_frame_equal(left, right, check_index_type=check_index_type)
    df = pd.DataFrame({'jim': list('B' * 4 + 'A' * 2 + 'C' * 3), 'joe': list('abcdeabcd')[::-1], 'jolie': [10, 20, 30] * 3, 'joline': np.random.randint(0, 1000, 9)})
    target = [['C', 'B', 'A'], ['F', 'C', 'A', 'D'], ['A'], ['A', 'B', 'C'], ['C', 'A', 'B'], ['C', 'B'], ['C', 'A'], ['A', 'B'], ['B', 'A', 'C']]
    for idx in target:
        verify_first_level(df, 'jim', idx)
    for idx in [['D', 'F'], ['A', 'C', 'B']]:
        verify_first_level(df, 'jim', idx, check_index_type=False)
    verify(df, 'joe', list('abcde'), [3, 2, 1, 0, 5, 4, 8, 7, 6])
    verify(df, 'joe', list('abcd'), [3, 2, 1, 0, 5, 8, 7, 6])
    verify(df, 'joe', list('abc'), [3, 2, 1, 8, 7, 6])
    verify(df, 'joe', list('eca'), [1, 3, 4, 6, 8])
    verify(df, 'joe', list('edc'), [0, 1, 4, 5, 6])
    verify(df, 'joe', list('eadbc'), [3, 0, 2, 1, 4, 5, 8, 7, 6])
    verify(df, 'joe', list('edwq'), [0, 4, 5])
    verify(df, 'joe', list('wq'), [], check_index_type=False)
    df = DataFrame({'jim': ['mid'] * 5 + ['btm'] * 8 + ['top'] * 7, 'joe': ['3rd'] * 2 + ['1st'] * 3 + ['2nd'] * 3 + ['1st'] * 2 + ['3rd'] * 3 + ['1st'] * 2 + ['3rd'] * 3 + ['2nd'] * 2, 'jolie': np.concatenate([np.random.choice(1000, x, replace=False) for x in [2, 3, 3, 2, 3, 2, 3, 2]]), 'joline': np.random.randn(20).round(3) * 10})
    for idx in permutations(df['jim'].unique()):
        for i in range(3):
            verify_first_level(df, 'jim', idx[:i + 1])
    i = [2, 3, 4, 0, 1, 8, 9, 5, 6, 7, 10, 11, 12, 13, 14, 18, 19, 15, 16, 17]
    verify(df, 'joe', ['1st', '2nd', '3rd'], i)
    i = [0, 1, 2, 3, 4, 10, 11, 12, 5, 6, 7, 8, 9, 15, 16, 17, 18, 19, 13, 14]
    verify(df, 'joe', ['3rd', '2nd', '1st'], i)
    i = [0, 1, 5, 6, 7, 10, 11, 12, 18, 19, 15, 16, 17]
    verify(df, 'joe', ['2nd', '3rd'], i)
    i = [0, 1, 2, 3, 4, 10, 11, 12, 8, 9, 15, 16, 17, 13, 14]
    verify(df, 'joe', ['3rd', '1st'], i)