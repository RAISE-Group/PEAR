def test_corr_cov_independent_index_column(self):
    df = pd.DataFrame(np.random.randn(4 * 10).reshape(10, 4), columns=list('abcd'))
    for method in ['cov', 'corr']:
        result = getattr(df, method)()
        assert result.index is not result.columns
        assert result.index.equals(result.columns)