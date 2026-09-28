def test_reduce_invalid(self):
    data = np.arange(10, dtype='i8') * 24 * 3600 * 10 ** 9
    arr = self.array_cls(data, freq='D')
    with pytest.raises(TypeError, match='cannot perform'):
        arr._reduce('not a method')