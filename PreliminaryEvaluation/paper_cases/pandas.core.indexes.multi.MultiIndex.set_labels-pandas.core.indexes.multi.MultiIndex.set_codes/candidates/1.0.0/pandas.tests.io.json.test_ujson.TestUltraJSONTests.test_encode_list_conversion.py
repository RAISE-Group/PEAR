def test_encode_list_conversion(self):
    list_input = [1, 2, 3, 4]
    output = ujson.encode(list_input)
    assert list_input == json.loads(output)
    assert list_input == ujson.decode(output)
    tm.assert_numpy_array_equal(np.array(list_input), ujson.decode(output, numpy=True))