def test_convert_infs(self):
    arr = np.array(['inf', 'inf', 'inf'], dtype='O')
    result = lib.maybe_convert_numeric(arr, set(), False)
    assert result.dtype == np.float64
    arr = np.array(['-inf', '-inf', '-inf'], dtype='O')
    result = lib.maybe_convert_numeric(arr, set(), False)
    assert result.dtype == np.float64