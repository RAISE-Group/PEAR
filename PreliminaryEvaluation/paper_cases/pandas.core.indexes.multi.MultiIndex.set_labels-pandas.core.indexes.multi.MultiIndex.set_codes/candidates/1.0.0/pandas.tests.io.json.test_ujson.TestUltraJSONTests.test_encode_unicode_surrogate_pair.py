def test_encode_unicode_surrogate_pair(self):
    surrogate_input = 'ð\x90\x8d\x86'
    enc = ujson.encode(surrogate_input)
    dec = ujson.decode(enc)
    assert enc == json.dumps(surrogate_input)
    assert dec == json.loads(enc)