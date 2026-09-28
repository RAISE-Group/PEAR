def test_array_list(self):
    arr_list = ['a', list(), dict(), dict(), list(), 42, 97.8, ['a', 'b'], {'key': 'val'}]
    arr = np.array(arr_list, dtype=object)
    result = np.array(ujson.decode(ujson.encode(arr)), dtype=object)
    tm.assert_numpy_array_equal(result, arr)