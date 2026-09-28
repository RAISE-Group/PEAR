def test_decimal_decode_test_precise(self):
    sut = {'a': 4.56}
    encoded = ujson.encode(sut)
    decoded = ujson.decode(encoded, precise_float=True)
    assert sut == decoded