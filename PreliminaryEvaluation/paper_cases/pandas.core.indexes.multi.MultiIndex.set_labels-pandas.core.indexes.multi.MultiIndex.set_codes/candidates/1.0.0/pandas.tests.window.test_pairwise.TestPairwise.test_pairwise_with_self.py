@pytest.mark.parametrize('f', [lambda x: x.expanding().cov(pairwise=True), lambda x: x.expanding().corr(pairwise=True), lambda x: x.rolling(window=3).cov(pairwise=True), lambda x: x.rolling(window=3).corr(pairwise=True), lambda x: x.ewm(com=3).cov(pairwise=True), lambda x: x.ewm(com=3).corr(pairwise=True)])
def test_pairwise_with_self(self, f):
    results = []
    for i, df in enumerate(self.df1s):
        result = f(df)
        tm.assert_index_equal(result.index.levels[0], df.index, check_names=False)
        tm.assert_numpy_array_equal(safe_sort(result.index.levels[1]), safe_sort(df.columns.unique()))
        tm.assert_index_equal(result.columns, df.columns)
        results.append(df)
    for i, result in enumerate(results):
        if i > 0:
            self.compare(result, results[0])