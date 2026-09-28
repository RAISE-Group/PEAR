@pytest.mark.parametrize('f', [lambda x, y: x.expanding().cov(y, pairwise=True), lambda x, y: x.expanding().corr(y, pairwise=True), lambda x, y: x.rolling(window=3).cov(y, pairwise=True), lambda x, y: x.rolling(window=3).corr(y, pairwise=True), lambda x, y: x.ewm(com=3).cov(y, pairwise=True), lambda x, y: x.ewm(com=3).corr(y, pairwise=True)])
def test_pairwise_with_other(self, f):
    results = [f(df, self.df2) for df in self.df1s]
    for df, result in zip(self.df1s, results):
        tm.assert_index_equal(result.index.levels[0], df.index, check_names=False)
        tm.assert_numpy_array_equal(safe_sort(result.index.levels[1]), safe_sort(self.df2.columns.unique()))
    for i, result in enumerate(results):
        if i > 0:
            self.compare(result, results[0])