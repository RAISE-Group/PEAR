def test_float_max(self, float_dtype):
    klass = np.dtype(float_dtype).type
    num = klass(np.finfo(float_dtype).max / 10)
    tm.assert_almost_equal(klass(ujson.decode(ujson.encode(num, double_precision=15))), num)