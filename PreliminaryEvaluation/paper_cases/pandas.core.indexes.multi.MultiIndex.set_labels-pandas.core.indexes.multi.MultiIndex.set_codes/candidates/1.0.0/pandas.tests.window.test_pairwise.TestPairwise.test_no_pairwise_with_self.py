@pytest.mark.parametrize('f', [lambda x: x.expanding().cov(pairwise=False), lambda x: x.expanding().corr(pairwise=False), lambda x: x.rolling(window=3).cov(pairwise=False), lambda x: x.rolling(window=3).corr(pairwise=False), lambda x: x.ewm(com=3).cov(pairwise=False), lambda x: x.ewm(com=3).corr(pairwise=False)])
def test_no_pairwise_with_self(self, f):
    results = [f(df) for df in self.df1s]
    for df, result in zip(self.df1s, results):
        tm.assert_index_equal(result.index, df.index)
        tm.assert_index_equal(result.columns, df.columns)
    for i, result in enumerate(results):
        if i > 0:
            self.compare(result, results[0])