@pytest.mark.parametrize('num_input', [31337, -31337, -9223372036854775808])
def test_encode_num_conversion(self, num_input):
    output = ujson.encode(num_input)
    assert num_input == json.loads(output)
    assert output == json.dumps(num_input)
    assert num_input == ujson.decode(output)