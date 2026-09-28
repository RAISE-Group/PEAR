def test_rank_methods_series(self):
    pytest.importorskip('scipy.stats.special')
    rankdata = pytest.importorskip('scipy.stats.rankdata')
    xs = np.random.randn(9)
    xs = np.concatenate([xs[i:] for i in range(0, 9, 2)])
    np.random.shuffle(xs)
    index = [chr(ord('a') + i) for i in range(len(xs))]
    for vals in [xs, xs + 1000000.0, xs * 1e-06]:
        ts = Series(vals, index=index)
        for m in ['average', 'min', 'max', 'first', 'dense']:
            result = ts.rank(method=m)
            sprank = rankdata(vals, m if m != 'first' else 'ordinal')
            expected = Series(sprank, index=index).astype('float64')
            tm.assert_series_equal(result, expected)