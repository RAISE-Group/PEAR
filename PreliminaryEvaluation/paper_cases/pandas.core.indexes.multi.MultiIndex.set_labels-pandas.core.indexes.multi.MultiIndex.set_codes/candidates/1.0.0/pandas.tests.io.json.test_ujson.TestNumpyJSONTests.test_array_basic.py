def test_array_basic(self):
    arr = np.arange(96)
    arr = arr.reshape((2, 2, 2, 2, 3, 2))
    tm.assert_numpy_array_equal(np.array(ujson.decode(ujson.encode(arr))), arr)
    tm.assert_numpy_array_equal(ujson.decode(ujson.encode(arr), numpy=True), arr)