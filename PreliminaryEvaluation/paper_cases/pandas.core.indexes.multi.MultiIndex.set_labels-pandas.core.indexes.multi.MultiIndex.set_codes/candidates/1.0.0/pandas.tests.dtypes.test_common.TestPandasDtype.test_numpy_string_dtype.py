def test_numpy_string_dtype(self):
    assert com.pandas_dtype('U') == np.dtype('U')
    assert com.pandas_dtype('S') == np.dtype('S')