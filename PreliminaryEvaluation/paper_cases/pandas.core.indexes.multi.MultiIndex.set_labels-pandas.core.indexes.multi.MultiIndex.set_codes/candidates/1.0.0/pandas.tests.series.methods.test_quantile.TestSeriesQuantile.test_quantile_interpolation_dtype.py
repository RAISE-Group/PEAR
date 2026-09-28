def test_quantile_interpolation_dtype(self):
    q = pd.Series([1, 3, 4]).quantile(0.5, interpolation='lower')
    assert q == np.percentile(np.array([1, 3, 4]), 50)
    assert is_integer(q)
    q = pd.Series([1, 3, 4]).quantile(0.5, interpolation='higher')
    assert q == np.percentile(np.array([1, 3, 4]), 50)
    assert is_integer(q)