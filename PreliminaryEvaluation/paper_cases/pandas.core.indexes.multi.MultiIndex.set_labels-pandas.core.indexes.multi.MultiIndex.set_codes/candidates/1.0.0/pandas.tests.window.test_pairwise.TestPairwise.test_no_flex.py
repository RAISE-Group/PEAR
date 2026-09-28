@pytest.mark.parametrize('f', [lambda x: x.cov(), lambda x: x.corr()])
def test_no_flex(self, f):
    results = [f(df) for df in self.df1s]
    for df, result in zip(self.df1s, results):
        tm.assert_index_equal(result.index, df.columns)
        tm.assert_index_equal(result.columns, df.columns)
    for i, result in enumerate(results):
        if i > 0:
            self.compare(result, results[0])