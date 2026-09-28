def test_encode_to_utf8(self):
    unencoded = 'æ\x97¥Ñ\x88'
    enc = ujson.encode(unencoded, ensure_ascii=False)
    dec = ujson.decode(enc)
    assert enc == json.dumps(unencoded, ensure_ascii=False)
    assert dec == json.loads(enc)