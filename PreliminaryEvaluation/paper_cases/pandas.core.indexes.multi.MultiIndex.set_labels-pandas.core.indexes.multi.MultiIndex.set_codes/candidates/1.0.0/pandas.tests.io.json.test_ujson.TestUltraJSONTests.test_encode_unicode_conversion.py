@pytest.mark.parametrize('unicode_input', ['Räksmörgås اسامة بن محمد بن عوض بن لادن', 'æ\x97¥Ñ\x88'])
def test_encode_unicode_conversion(self, unicode_input):
    enc = ujson.encode(unicode_input)
    dec = ujson.decode(enc)
    assert enc == json.dumps(unicode_input)
    assert dec == json.loads(enc)