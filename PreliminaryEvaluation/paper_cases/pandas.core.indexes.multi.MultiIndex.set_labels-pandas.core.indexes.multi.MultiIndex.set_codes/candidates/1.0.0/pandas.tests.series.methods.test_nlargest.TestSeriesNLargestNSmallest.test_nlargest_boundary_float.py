def test_nlargest_boundary_float(self, nselect_method, float_dtype):
    dtype_info = np.finfo(float_dtype)
    min_val, max_val = (dtype_info.min, dtype_info.max)
    min_2nd, max_2nd = np.nextafter([min_val, max_val], 0, dtype=float_dtype)
    vals = [min_val, min_2nd, max_2nd, max_val]
    assert_check_nselect_boundary(vals, float_dtype, nselect_method)