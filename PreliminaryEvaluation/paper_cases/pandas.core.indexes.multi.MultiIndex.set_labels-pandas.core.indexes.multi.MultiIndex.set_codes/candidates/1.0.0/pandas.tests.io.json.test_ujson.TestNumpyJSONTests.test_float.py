def test_float(self, float_dtype):
    klass = np.dtype(float_dtype).type
    num = klass(256.2013)
    assert klass(ujson.decode(ujson.encode(num))) == num