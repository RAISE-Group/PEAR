def test_encode_unicode_4bytes_utf8highest(self):
    four_bytes_input = 'ó¿¿¿TRAILINGNORMAL'
    enc = ujson.encode(four_bytes_input)
    dec = ujson.decode(enc)
    assert enc == json.dumps(four_bytes_input)
    assert dec == json.loads(enc)