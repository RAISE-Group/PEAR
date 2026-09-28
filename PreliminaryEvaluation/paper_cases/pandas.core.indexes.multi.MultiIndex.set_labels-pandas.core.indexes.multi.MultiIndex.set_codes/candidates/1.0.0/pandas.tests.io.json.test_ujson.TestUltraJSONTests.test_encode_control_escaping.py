def test_encode_control_escaping(self):
    escaped_input = '\x19'
    enc = ujson.encode(escaped_input)
    dec = ujson.decode(enc)
    assert escaped_input == dec
    assert enc == json.dumps(escaped_input)