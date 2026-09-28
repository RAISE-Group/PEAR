def test_encode_array_of_doubles(self):
    doubles_input = [31337.31337, 31337.31337, 31337.31337, 31337.31337] * 10
    output = ujson.encode(doubles_input)
    assert doubles_input == json.loads(output)
    assert doubles_input == ujson.decode(output)
    tm.assert_numpy_array_equal(np.array(doubles_input), ujson.decode(output, numpy=True))