def test_float_array(self, float_dtype):
    arr = np.arange(12.5, 185.72, 1.7322, dtype=np.float)
    float_input = arr.astype(float_dtype)
    float_output = np.array(ujson.decode(ujson.encode(float_input, double_precision=15)), dtype=float_dtype)
    tm.assert_almost_equal(float_input, float_output)