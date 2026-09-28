def test_int_array(self, any_int_dtype):
    arr = np.arange(100, dtype=np.int)
    arr_input = arr.astype(any_int_dtype)
    arr_output = np.array(ujson.decode(ujson.encode(arr_input)), dtype=any_int_dtype)
    tm.assert_numpy_array_equal(arr_input, arr_output)