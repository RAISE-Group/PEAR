@pytest.mark.parametrize('dtype', [object, np.int32, np.int64])
def test_constructor_invalid_dtype_raises(self, dtype):
    with pytest.raises(ValueError):
        DatetimeIndex([1, 2], dtype=dtype)