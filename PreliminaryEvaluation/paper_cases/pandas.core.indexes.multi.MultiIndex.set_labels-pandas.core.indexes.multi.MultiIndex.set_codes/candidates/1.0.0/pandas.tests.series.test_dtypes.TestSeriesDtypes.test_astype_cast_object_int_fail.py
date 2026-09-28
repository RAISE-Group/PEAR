@pytest.mark.parametrize('dtype', [int, np.int8, np.int64])
def test_astype_cast_object_int_fail(self, dtype):
    arr = Series(['car', 'house', 'tree', '1'])
    msg = "invalid literal for int\\(\\) with base 10: 'car'"
    with pytest.raises(ValueError, match=msg):
        arr.astype(dtype)