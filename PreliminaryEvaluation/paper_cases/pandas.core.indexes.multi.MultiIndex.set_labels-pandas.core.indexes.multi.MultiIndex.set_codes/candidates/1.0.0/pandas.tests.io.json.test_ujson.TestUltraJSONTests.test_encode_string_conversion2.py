def test_encode_string_conversion2(self):
    string_input = 'A string \\ / \x08 \x0c \n \r \t'
    output = ujson.encode(string_input)
    assert string_input == json.loads(output)
    assert string_input == ujson.decode(output)
    assert output == '"A string \\\\ \\/ \\b \\f \\n \\r \\t"'