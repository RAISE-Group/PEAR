def test_encode_list_long_conversion(self):
    long_input = [9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807, 9223372036854775807]
    output = ujson.encode(long_input)
    assert long_input == json.loads(output)
    assert long_input == ujson.decode(output)
    tm.assert_numpy_array_equal(np.array(long_input), ujson.decode(output, numpy=True, dtype=np.int64))