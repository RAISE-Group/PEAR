def test_encode_array_in_array(self):
    arr_in_arr_input = [[[[]]]]
    output = ujson.encode(arr_in_arr_input)
    assert arr_in_arr_input == json.loads(output)
    assert output == json.dumps(arr_in_arr_input)
    assert arr_in_arr_input == ujson.decode(output)
    tm.assert_numpy_array_equal(np.array(arr_in_arr_input), ujson.decode(output, numpy=True))