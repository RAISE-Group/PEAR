def test_encode_long_conversion(self):
    long_input = 9223372036854775807
    output = ujson.encode(long_input)
    assert long_input == json.loads(output)
    assert output == json.dumps(long_input)
    assert long_input == ujson.decode(output)