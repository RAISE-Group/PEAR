def test_nlargest_boundary_integer(self, nselect_method, any_int_dtype):
    dtype_info = np.iinfo(any_int_dtype)
    min_val, max_val = (dtype_info.min, dtype_info.max)
    vals = [min_val, min_val + 1, max_val - 1, max_val]
    assert_check_nselect_boundary(vals, any_int_dtype, nselect_method)