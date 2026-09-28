def test_corr_invalid_method(self):
    df = pd.DataFrame(np.random.normal(size=(10, 2)))
    msg = "method must be either 'pearson', 'spearman', 'kendall', or a callable, "
    with pytest.raises(ValueError, match=msg):
        df.corr(method='____')