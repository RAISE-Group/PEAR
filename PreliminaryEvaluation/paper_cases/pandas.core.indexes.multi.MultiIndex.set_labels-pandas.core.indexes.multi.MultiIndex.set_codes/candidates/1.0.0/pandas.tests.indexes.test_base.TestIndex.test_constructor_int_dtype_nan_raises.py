@pytest.mark.parametrize('dtype', ['int64', 'uint64'])
def test_constructor_int_dtype_nan_raises(self, dtype):
    data = [np.nan]
    msg = 'cannot convert'
    with pytest.raises(ValueError, match=msg):
        Index(data, dtype=dtype)