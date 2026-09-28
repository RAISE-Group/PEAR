def test_encode_empty_set(self):
    assert '[]' == ujson.encode(set())