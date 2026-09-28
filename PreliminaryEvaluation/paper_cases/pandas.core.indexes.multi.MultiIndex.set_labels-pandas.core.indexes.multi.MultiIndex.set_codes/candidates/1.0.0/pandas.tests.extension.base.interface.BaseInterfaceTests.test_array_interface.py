def test_array_interface(self, data):
    result = np.array(data)
    assert result[0] == data[0]
    result = np.array(data, dtype=object)
    expected = np.array(list(data), dtype=object)
    tm.assert_numpy_array_equal(result, expected)