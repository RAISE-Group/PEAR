def test_setindex(self, string_series):
    msg = 'Index\\(\\.\\.\\.\\) must be called with a collection of some kind, None was passed'
    with pytest.raises(TypeError, match=msg):
        string_series.index = None
    msg = 'Length mismatch: Expected axis has 30 elements, new values have 29 elements'
    with pytest.raises(ValueError, match=msg):
        string_series.index = np.arange(len(string_series) - 1)
    string_series.index = np.arange(len(string_series))
    assert isinstance(string_series.index, Index)