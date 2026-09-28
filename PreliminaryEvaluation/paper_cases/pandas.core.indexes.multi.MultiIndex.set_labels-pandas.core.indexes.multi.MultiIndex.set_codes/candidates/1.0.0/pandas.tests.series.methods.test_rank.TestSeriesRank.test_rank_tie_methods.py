def test_rank_tie_methods(self):
    s = self.s

    def _check(s, expected, method='average'):
        result = s.rank(method=method)
        tm.assert_series_equal(result, Series(expected))
    dtypes = [None, object]
    disabled = {(object, 'first')}
    results = self.results
    for method, dtype in product(results, dtypes):
        if (dtype, method) in disabled:
            continue
        series = s if dtype is None else s.astype(dtype)
        _check(series, results[method], method=method)