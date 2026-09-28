def test_int64_overflow_moar(self):
    values = range(55109)
    data = DataFrame.from_dict({'a': values, 'b': values, 'c': values, 'd': values})
    grouped = data.groupby(['a', 'b', 'c', 'd'])
    assert len(grouped) == len(values)
    arr = np.random.randint(-1 << 12, 1 << 12, (1 << 15, 5))
    i = np.random.choice(len(arr), len(arr) * 4)
    arr = np.vstack((arr, arr[i]))
    i = np.random.permutation(len(arr))
    arr = arr[i]
    df = DataFrame(arr, columns=list('abcde'))
    df['jim'], df['joe'] = np.random.randn(2, len(df)) * 10
    gr = df.groupby(list('abcde'))
    assert is_int64_overflow_possible(gr.grouper.shape)
    jim, joe = (defaultdict(list), defaultdict(list))
    for key, a, b in zip(map(tuple, arr), df['jim'], df['joe']):
        jim[key].append(a)
        joe[key].append(b)
    assert len(gr) == len(jim)
    mi = MultiIndex.from_tuples(jim.keys(), names=list('abcde'))

    def aggr(func):
        f = lambda a: np.fromiter(map(func, a), dtype='f8')
        arr = np.vstack((f(jim.values()), f(joe.values()))).T
        res = DataFrame(arr, columns=['jim', 'joe'], index=mi)
        return res.sort_index()
    tm.assert_frame_equal(gr.mean(), aggr(np.mean))
    tm.assert_frame_equal(gr.median(), aggr(np.median))