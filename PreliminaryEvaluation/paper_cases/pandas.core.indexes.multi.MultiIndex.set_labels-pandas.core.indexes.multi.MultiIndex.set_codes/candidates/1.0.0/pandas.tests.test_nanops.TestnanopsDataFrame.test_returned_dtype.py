@pytest.mark.parametrize('dtype', [np.int16, np.int32, np.int64, np.float32, np.float64, getattr(np, 'float128', None)])
def test_returned_dtype(self, dtype):
    if dtype is None:
        return
    s = Series(range(10), dtype=dtype)
    group_a = ['mean', 'std', 'var', 'skew', 'kurt']
    group_b = ['min', 'max']
    for method in group_a + group_b:
        result = getattr(s, method)()
        if is_integer_dtype(dtype) and method in group_a:
            assert result.dtype == np.float64
        else:
            assert result.dtype == dtype