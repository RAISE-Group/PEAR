def test_array_float(self):
    dtype = np.float32
    arr = np.arange(100.202, 200.202, 1, dtype=dtype)
    arr = arr.reshape((5, 5, 4))
    arr_out = np.array(ujson.decode(ujson.encode(arr)), dtype=dtype)
    tm.assert_almost_equal(arr, arr_out)
    arr_out = ujson.decode(ujson.encode(arr), numpy=True, dtype=dtype)
    tm.assert_almost_equal(arr, arr_out)