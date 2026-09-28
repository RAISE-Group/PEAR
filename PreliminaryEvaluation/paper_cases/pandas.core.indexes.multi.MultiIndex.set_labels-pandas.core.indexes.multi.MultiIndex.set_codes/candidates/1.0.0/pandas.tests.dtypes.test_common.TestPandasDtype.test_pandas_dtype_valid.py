@pytest.mark.parametrize('dtype', [object, 'float64', np.object_, np.dtype('object'), 'O', np.float64, float, np.dtype('float64')])
def test_pandas_dtype_valid(self, dtype):
    assert com.pandas_dtype(dtype) == dtype