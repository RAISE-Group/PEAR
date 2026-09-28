def test_corr_invalid_method(self):
    s1 = pd.Series(np.random.randn(10))
    s2 = pd.Series(np.random.randn(10))
    msg = "method must be either 'pearson', 'spearman', 'kendall', or a callable, "
    with pytest.raises(ValueError, match=msg):
        s1.corr(s2, method='____')