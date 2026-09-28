def test_decode_from_unicode(self):
    unicode_input = '{"obj": 31337}'
    dec1 = ujson.decode(unicode_input)
    dec2 = ujson.decode(str(unicode_input))
    assert dec1 == dec2