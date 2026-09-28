def test_setitem_raises(self):
    data = np.arange(10, dtype='i8') * 24 * 3600 * 10 ** 9
    arr = self.array_cls(data, freq='D')
    val = arr[0]
    with pytest.raises(IndexError, match='index 12 is out of bounds'):
        arr[12] = val
    with pytest.raises(TypeError, match="'value' should be a.* 'object'"):
        arr[0] = object()