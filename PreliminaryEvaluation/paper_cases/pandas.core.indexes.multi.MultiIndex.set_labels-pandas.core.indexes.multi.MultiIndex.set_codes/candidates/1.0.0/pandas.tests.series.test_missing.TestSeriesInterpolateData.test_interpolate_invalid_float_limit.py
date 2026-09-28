def test_interpolate_invalid_float_limit(self, nontemporal_method):
    s = pd.Series([1, 2, np.nan, 4])
    method, kwargs = nontemporal_method
    limit = 2.0
    with pytest.raises(ValueError, match='Limit must be an integer'):
        s.interpolate(limit=limit, method=method, **kwargs)