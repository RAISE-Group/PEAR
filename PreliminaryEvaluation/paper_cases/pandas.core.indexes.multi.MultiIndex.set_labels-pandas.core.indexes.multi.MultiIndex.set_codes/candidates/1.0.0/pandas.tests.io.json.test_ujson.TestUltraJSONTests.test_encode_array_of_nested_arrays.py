def test_encode_array_of_nested_arrays(self):
    nested_input = [[[[]]]] * 20
    output = ujson.encode(nested_input)
    assert nested_input == json.loads(output)
    assert nested_input == ujson.decode(output)
    nested_input = np.array(nested_input)
    tm.assert_numpy_array_equal(nested_input, ujson.decode(output, numpy=True, dtype=nested_input.dtype))