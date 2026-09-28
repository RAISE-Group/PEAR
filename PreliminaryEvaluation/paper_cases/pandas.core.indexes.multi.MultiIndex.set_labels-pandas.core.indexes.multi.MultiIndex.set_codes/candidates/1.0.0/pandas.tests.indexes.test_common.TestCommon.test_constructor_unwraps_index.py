def test_constructor_unwraps_index(self, indices):
    if isinstance(indices, pd.MultiIndex):
        raise pytest.skip('MultiIndex has no ._data')
    a = indices
    b = type(a)(a)
    tm.assert_equal(a._data, b._data)