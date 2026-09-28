def test_decode_with_trailing_whitespaces(self):
    assert {} == ujson.decode('{}\n\t ')