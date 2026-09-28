@pytest.mark.parametrize('dtype', ['bool', 'int32', 'int64', 'float64'])
def test_constructor_index_dtype(self, dtype):
    s = Series(Index([0, 2, 4]), dtype=dtype)
    assert s.dtype == dtype