@pytest.mark.parametrize('dtype', ['M8[ns]', 'm8[ns]', 'object', 'float64', 'int64'])
def test_numpy_dtype(self, dtype):
    assert com.pandas_dtype(dtype) == np.dtype(dtype)