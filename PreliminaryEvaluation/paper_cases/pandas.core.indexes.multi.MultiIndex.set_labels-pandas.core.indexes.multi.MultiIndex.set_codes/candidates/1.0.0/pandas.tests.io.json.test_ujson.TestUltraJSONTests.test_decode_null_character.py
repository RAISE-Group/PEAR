def test_decode_null_character(self):
    wrapped_input = '"31337 \\u0000 31337"'
    assert ujson.decode(wrapped_input) == json.loads(wrapped_input)