@pytest.mark.slow
def test_int64_overflow_issues(self):
    df1 = DataFrame(np.random.randn(1000, 7), columns=list('ABCDEF') + ['G1'])
    df2 = DataFrame(np.random.randn(1000, 7), columns=list('ABCDEF') + ['G2'])
    result = merge(df1, df2, how='outer')
    assert len(result) == 2000
    low, high, n = (-1 << 10, 1 << 10, 1 << 20)
    left = DataFrame(np.random.randint(low, high, (n, 7)), columns=list('ABCDEFG'))
    left['left'] = left.sum(axis=1)
    i = np.random.permutation(len(left))
    right = left.iloc[i].copy()
    right.columns = right.columns[:-1].tolist() + ['right']
    right.index = np.arange(len(right))
    right['right'] *= -1
    out = merge(left, right, how='outer')
    assert len(out) == len(left)
    tm.assert_series_equal(out['left'], -out['right'], check_names=False)
    result = out.iloc[:, :-2].sum(axis=1)
    tm.assert_series_equal(out['left'], result, check_names=False)
    assert result.name is None
    out.sort_values(out.columns.tolist(), inplace=True)
    out.index = np.arange(len(out))
    for how in ['left', 'right', 'outer', 'inner']:
        tm.assert_frame_equal(out, merge(left, right, how=how, sort=True))
    out = merge(left, right, how='left', sort=False)
    tm.assert_frame_equal(left, out[left.columns.tolist()])
    out = merge(right, left, how='left', sort=False)
    tm.assert_frame_equal(right, out[right.columns.tolist()])
    n = 1 << 11
    left = DataFrame(np.random.randint(low, high, (n, 7)).astype('int64'), columns=list('ABCDEFG'))
    shape = left.apply(Series.nunique).values
    assert is_int64_overflow_possible(shape)
    left = concat([left, left], ignore_index=True)
    right = DataFrame(np.random.randint(low, high, (n // 2, 7)).astype('int64'), columns=list('ABCDEFG'))
    i = np.random.choice(len(left), n)
    right = concat([right, right, left.iloc[i]], ignore_index=True)
    left['left'] = np.random.randn(len(left))
    right['right'] = np.random.randn(len(right))
    i = np.random.permutation(len(left))
    left = left.iloc[i].copy()
    left.index = np.arange(len(left))
    i = np.random.permutation(len(right))
    right = right.iloc[i].copy()
    right.index = np.arange(len(right))
    ldict, rdict = (defaultdict(list), defaultdict(list))
    for idx, row in left.set_index(list('ABCDEFG')).iterrows():
        ldict[idx].append(row['left'])
    for idx, row in right.set_index(list('ABCDEFG')).iterrows():
        rdict[idx].append(row['right'])
    vals = []
    for k, lval in ldict.items():
        rval = rdict.get(k, [np.nan])
        for lv, rv in product(lval, rval):
            vals.append(k + tuple([lv, rv]))
    for k, rval in rdict.items():
        if k not in ldict:
            for rv in rval:
                vals.append(k + tuple([np.nan, rv]))

    def align(df):
        df = df.sort_values(df.columns.tolist())
        df.index = np.arange(len(df))
        return df

    def verify_order(df):
        kcols = list('ABCDEFG')
        tm.assert_frame_equal(df[kcols].copy(), df[kcols].sort_values(kcols, kind='mergesort'))
    out = DataFrame(vals, columns=list('ABCDEFG') + ['left', 'right'])
    out = align(out)
    jmask = {'left': out['left'].notna(), 'right': out['right'].notna(), 'inner': out['left'].notna() & out['right'].notna(), 'outer': np.ones(len(out), dtype='bool')}
    for how in ('left', 'right', 'outer', 'inner'):
        mask = jmask[how]
        frame = align(out[mask].copy())
        assert mask.all() ^ mask.any() or how == 'outer'
        for sort in [False, True]:
            res = merge(left, right, how=how, sort=sort)
            if sort:
                verify_order(res)
            tm.assert_frame_equal(frame, align(res), check_dtype=how not in ('right', 'outer'))