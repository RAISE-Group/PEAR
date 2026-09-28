@pytest.mark.parametrize('f', [lambda x, y: x.expanding().cov(y), lambda x, y: x.expanding().corr(y), lambda x, y: x.rolling(window=3).cov(y), lambda x, y: x.rolling(window=3).corr(y), lambda x, y: x.ewm(com=3).cov(y), lambda x, y: x.ewm(com=3).corr(y)])
def test_pairwise_with_series(self, f):
    results = [f(df, self.s) for df in self.df1s] + [f(self.s, df) for df in self.df1s]
    for df, result in zip(self.df1s, results):
        tm.assert_index_equal(result.index, df.index)
        tm.assert_index_equal(result.columns, df.columns)
    for i, result in enumerate(results):
        if i > 0:
            self.compare(result, results[0])