def test_encode_double_tiny_exponential(self):
    num = 1e-40
    assert num == ujson.decode(ujson.encode(num))
    num = 1e-100
    assert num == ujson.decode(ujson.encode(num))
    num = -1e-45
    assert num == ujson.decode(ujson.encode(num))
    num = -1e-145
    assert np.allclose(num, ujson.decode(ujson.encode(num)))