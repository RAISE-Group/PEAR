def test_unstack_nan_index(self):
    cast = lambda val: '{0:1}'.format('' if val != val else val)

    def verify(df):
        mk_list = lambda a: list(a) if isinstance(a, tuple) else [a]
        rows, cols = df.notna().values.nonzero()
        for i, j in zip(rows, cols):
            left = sorted(df.iloc[i, j].split('.'))
            right = mk_list(df.index[i]) + mk_list(df.columns[j])
            right = sorted(map(cast, right))
            assert left == right
    df = DataFrame({'jim': ['a', 'b', np.nan, 'd'], 'joe': ['w', 'x', 'y', 'z'], 'jolie': ['a.w', 'b.x', ' .y', 'd.z']})
    left = df.set_index(['jim', 'joe']).unstack()['jolie']
    right = df.set_index(['joe', 'jim']).unstack()['jolie'].T
    tm.assert_frame_equal(left, right)
    for idx in itertools.permutations(df.columns[:2]):
        mi = df.set_index(list(idx))
        for lev in range(2):
            udf = mi.unstack(level=lev)
            assert udf.notna().values.sum() == len(df)
            verify(udf['jolie'])
    df = DataFrame({'1st': ['d'] * 3 + [np.nan] * 5 + ['a'] * 2 + ['c'] * 3 + ['e'] * 2 + ['b'] * 5, '2nd': ['y'] * 2 + ['w'] * 3 + [np.nan] * 3 + ['z'] * 4 + [np.nan] * 3 + ['x'] * 3 + [np.nan] * 2, '3rd': [67, 39, 53, 72, 57, 80, 31, 18, 11, 30, 59, 50, 62, 59, 76, 52, 14, 53, 60, 51]})
    df['4th'], df['5th'] = (df.apply(lambda r: '.'.join(map(cast, r)), axis=1), df.apply(lambda r: '.'.join(map(cast, r.iloc[::-1])), axis=1))
    for idx in itertools.permutations(['1st', '2nd', '3rd']):
        mi = df.set_index(list(idx))
        for lev in range(3):
            udf = mi.unstack(level=lev)
            assert udf.notna().values.sum() == 2 * len(df)
            for col in ['4th', '5th']:
                verify(udf[col])
    df = pd.DataFrame({'A': list('aaaabbbb'), 'B': range(8), 'C': range(8)})
    df.iloc[3, 1] = np.NaN
    left = df.set_index(['A', 'B']).unstack(0)
    vals = [[3, 0, 1, 2, np.nan, np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan, np.nan, 4, 5, 6, 7]]
    vals = list(map(list, zip(*vals)))
    idx = Index([np.nan, 0, 1, 2, 4, 5, 6, 7], name='B')
    cols = MultiIndex(levels=[['C'], ['a', 'b']], codes=[[0, 0], [0, 1]], names=[None, 'A'])
    right = DataFrame(vals, columns=cols, index=idx)
    tm.assert_frame_equal(left, right)
    df = DataFrame({'A': list('aaaabbbb'), 'B': list(range(4)) * 2, 'C': range(8)})
    df.iloc[2, 1] = np.NaN
    left = df.set_index(['A', 'B']).unstack(0)
    vals = [[2, np.nan], [0, 4], [1, 5], [np.nan, 6], [3, 7]]
    cols = MultiIndex(levels=[['C'], ['a', 'b']], codes=[[0, 0], [0, 1]], names=[None, 'A'])
    idx = Index([np.nan, 0, 1, 2, 3], name='B')
    right = DataFrame(vals, columns=cols, index=idx)
    tm.assert_frame_equal(left, right)
    df = pd.DataFrame({'A': list('aaaabbbb'), 'B': list(range(4)) * 2, 'C': range(8)})
    df.iloc[3, 1] = np.NaN
    left = df.set_index(['A', 'B']).unstack(0)
    vals = [[3, np.nan], [0, 4], [1, 5], [2, 6], [np.nan, 7]]
    cols = MultiIndex(levels=[['C'], ['a', 'b']], codes=[[0, 0], [0, 1]], names=[None, 'A'])
    idx = Index([np.nan, 0, 1, 2, 3], name='B')
    right = DataFrame(vals, columns=cols, index=idx)
    tm.assert_frame_equal(left, right)
    df = pd.DataFrame({'A': list('aaaaabbbbb'), 'B': date_range('2012-01-01', periods=5).tolist() * 2, 'C': np.arange(10)})
    df.iloc[3, 1] = np.NaN
    left = df.set_index(['A', 'B']).unstack()
    vals = np.array([[3, 0, 1, 2, np.nan, 4], [np.nan, 5, 6, 7, 8, 9]])
    idx = Index(['a', 'b'], name='A')
    cols = MultiIndex(levels=[['C'], date_range('2012-01-01', periods=5)], codes=[[0, 0, 0, 0, 0, 0], [-1, 0, 1, 2, 3, 4]], names=[None, 'B'])
    right = DataFrame(vals, columns=cols, index=idx)
    tm.assert_frame_equal(left, right)
    vals = [['Hg', np.nan, np.nan, 680585148], ['U', 0.0, np.nan, 680585148], ['Pb', 7.07e-06, np.nan, 680585148], ['Sn', 2.3614e-05, 0.0133, 680607017], ['Ag', 0.0, 0.0133, 680607017], ['Hg', -0.00015, 0.0133, 680607017]]
    df = DataFrame(vals, columns=['agent', 'change', 'dosage', 's_id'], index=[17263, 17264, 17265, 17266, 17267, 17268])
    left = df.copy().set_index(['s_id', 'dosage', 'agent']).unstack()
    vals = [[np.nan, np.nan, 7.07e-06, np.nan, 0.0], [0.0, -0.00015, np.nan, 2.3614e-05, np.nan]]
    idx = MultiIndex(levels=[[680585148, 680607017], [0.0133]], codes=[[0, 1], [-1, 0]], names=['s_id', 'dosage'])
    cols = MultiIndex(levels=[['change'], ['Ag', 'Hg', 'Pb', 'Sn', 'U']], codes=[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4]], names=[None, 'agent'])
    right = DataFrame(vals, columns=cols, index=idx)
    tm.assert_frame_equal(left, right)
    left = df.loc[17264:].copy().set_index(['s_id', 'dosage', 'agent'])
    tm.assert_frame_equal(left.unstack(), right)
    df = DataFrame({'1st': [1, 2, 1, 2, 1, 2], '2nd': pd.date_range('2014-02-01', periods=6, freq='D'), 'jim': 100 + np.arange(6), 'joe': (np.random.randn(6) * 10).round(2)})
    df['3rd'] = df['2nd'] - pd.Timestamp('2014-02-02')
    df.loc[1, '2nd'] = df.loc[3, '2nd'] = np.nan
    df.loc[1, '3rd'] = df.loc[4, '3rd'] = np.nan
    left = df.set_index(['1st', '2nd', '3rd']).unstack(['2nd', '3rd'])
    assert left.notna().values.sum() == 2 * len(df)
    for col in ['jim', 'joe']:
        for _, r in df.iterrows():
            key = (r['1st'], (col, r['2nd'], r['3rd']))
            assert r[col] == left.loc[key]