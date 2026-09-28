@pytest.mark.parametrize('invalid_method', [None, 'nonexistent_method'])
def test_interp_invalid_method(self, invalid_method):
    s = Series([1, 3, np.nan, 12, np.nan, 25])
    msg = f"method must be one of.* Got '{invalid_method}' instead"
    with pytest.raises(ValueError, match=msg):
        s.interpolate(method=invalid_method)
    with pytest.raises(ValueError, match=msg):
        s.interpolate(method=invalid_method, limit=-1)