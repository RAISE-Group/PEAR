@pytest.mark.parametrize('limit', [-1, 0])
def test_interpolate_invalid_nonpositive_limit(self, nontemporal_method, limit):
    s = pd.Series([1, 2, np.nan, 4])
    method, kwargs = nontemporal_method
    with pytest.raises(ValueError, match='Limit must be greater than 0'):
        s.interpolate(limit=limit, method=method, **kwargs)