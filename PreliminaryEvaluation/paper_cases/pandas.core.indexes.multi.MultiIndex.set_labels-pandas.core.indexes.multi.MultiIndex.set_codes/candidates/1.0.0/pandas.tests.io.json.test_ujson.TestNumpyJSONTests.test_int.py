def test_int(self, any_int_dtype):
    klass = np.dtype(any_int_dtype).type
    num = klass(1)
    assert klass(ujson.decode(ujson.encode(num))) == num