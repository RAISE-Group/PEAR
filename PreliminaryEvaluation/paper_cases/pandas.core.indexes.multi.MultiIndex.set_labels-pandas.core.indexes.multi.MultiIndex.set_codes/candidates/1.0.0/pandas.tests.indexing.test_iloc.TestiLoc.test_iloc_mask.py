def test_iloc_mask(self):
    df = DataFrame(list(range(5)), index=list('ABCDE'), columns=['a'])
    mask = df.a % 2 == 0
    msg = 'iLocation based boolean indexing cannot use an indexable as a mask'
    with pytest.raises(ValueError, match=msg):
        df.iloc[mask]
    mask.index = range(len(mask))
    msg = 'iLocation based boolean indexing on an integer type is not available'
    with pytest.raises(NotImplementedError, match=msg):
        df.iloc[mask]
    result = df.iloc[np.array([True] * len(mask), dtype=bool)]
    tm.assert_frame_equal(result, df)
    locs = np.arange(4)
    nums = 2 ** locs
    reps = [bin(num) for num in nums]
    df = DataFrame({'locs': locs, 'nums': nums}, reps)
    expected = {(None, ''): '0b1100', (None, '.loc'): '0b1100', (None, '.iloc'): '0b1100', ('index', ''): '0b11', ('index', '.loc'): '0b11', ('index', '.iloc'): 'iLocation based boolean indexing cannot use an indexable as a mask', ('locs', ''): 'Unalignable boolean Series provided as indexer (index of the boolean Series and of the indexed object do not match).', ('locs', '.loc'): 'Unalignable boolean Series provided as indexer (index of the boolean Series and of the indexed object do not match).', ('locs', '.iloc'): 'iLocation based boolean indexing on an integer type is not available'}
    with catch_warnings(record=True):
        simplefilter('ignore', UserWarning)
        result = dict()
        for idx in [None, 'index', 'locs']:
            mask = (df.nums > 2).values
            if idx:
                mask = Series(mask, list(reversed(getattr(df, idx))))
            for method in ['', '.loc', '.iloc']:
                try:
                    if method:
                        accessor = getattr(df, method[1:])
                    else:
                        accessor = df
                    ans = str(bin(accessor[mask]['nums'].sum()))
                except (ValueError, IndexingError, NotImplementedError) as e:
                    ans = str(e)
                key = tuple([idx, method])
                r = expected.get(key)
                if r != ans:
                    raise AssertionError('[{key}] does not match [{ans}], received [{r}]'.format(key=key, ans=ans, r=r))