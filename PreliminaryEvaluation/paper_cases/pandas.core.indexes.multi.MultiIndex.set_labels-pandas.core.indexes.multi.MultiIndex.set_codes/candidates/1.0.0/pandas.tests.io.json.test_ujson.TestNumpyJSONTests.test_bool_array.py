def test_bool_array(self):
    bool_array = np.array([True, False, True, True, False, True, False, False], dtype=np.bool)
    output = np.array(ujson.decode(ujson.encode(bool_array)), dtype=np.bool)
    tm.assert_numpy_array_equal(bool_array, output)