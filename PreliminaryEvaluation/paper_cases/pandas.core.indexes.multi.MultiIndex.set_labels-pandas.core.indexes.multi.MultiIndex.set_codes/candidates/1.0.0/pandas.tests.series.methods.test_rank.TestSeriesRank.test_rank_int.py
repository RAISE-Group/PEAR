def test_rank_int(self):
    s = self.s.dropna().astype('i8')
    for method, res in self.results.items():
        result = s.rank(method=method)
        expected = Series(res).dropna()
        expected.index = result.index
        tm.assert_series_equal(result, expected)