@pytest.mark.parametrize('f', [lambda x, y: x.expanding().cov(y, pairwise=False), lambda x, y: x.expanding().corr(y, pairwise=False), lambda x, y: x.rolling(window=3).cov(y, pairwise=False), lambda x, y: x.rolling(window=3).corr(y, pairwise=False), lambda x, y: x.ewm(com=3).cov(y, pairwise=False), lambda x, y: x.ewm(com=3).corr(y, pairwise=False)])
def test_no_pairwise_with_other(self, f):
    results = [f(df, self.df2) if df.columns.is_unique else None for df in self.df1s]
    for df, result in zip(self.df1s, results):
        if result is not None:
            with warnings.catch_warnings(record=True):
                warnings.simplefilter('ignore', RuntimeWarning)
                expected_index = df.index.union(self.df2.index)
                expected_columns = df.columns.union(self.df2.columns)
            tm.assert_index_equal(result.index, expected_index)
            tm.assert_index_equal(result.columns, expected_columns)
        else:
            with pytest.raises(ValueError, match="'arg1' columns are not unique"):
                f(df, self.df2)
            with pytest.raises(ValueError, match="'arg2' columns are not unique"):
                f(self.df2, df)