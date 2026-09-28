@pytest.mark.parametrize('dtype', ['float64', 'int64', 'bool'])
def test_to_numpy_na_raises(self, dtype):
    a = pd.array([0, 1, None], dtype='Int64')
    with pytest.raises(ValueError, match=dtype):
        a.to_numpy(dtype=dtype)