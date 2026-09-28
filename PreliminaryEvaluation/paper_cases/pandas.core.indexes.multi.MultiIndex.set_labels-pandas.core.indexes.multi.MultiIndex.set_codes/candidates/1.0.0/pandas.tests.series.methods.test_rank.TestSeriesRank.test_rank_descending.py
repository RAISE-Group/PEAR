def test_rank_descending(self):
    dtypes = ['O', 'f8', 'i8']
    for dtype, method in product(dtypes, self.results):
        if 'i' in dtype:
            s = self.s.dropna()
        else:
            s = self.s.astype(dtype)
        res = s.rank(ascending=False)
        expected = (s.max() - s).rank()
        tm.assert_series_equal(res, expected)
        if method == 'first' and dtype == 'O':
            continue
        expected = (s.max() - s).rank(method=method)
        res2 = s.rank(method=method, ascending=False)
        tm.assert_series_equal(res2, expected)