def test_compare_len1_raises(self):
    data = np.arange(10, dtype='i8') * 24 * 3600 * 10 ** 9
    idx = self.index_cls._simple_new(data, freq='D')
    arr = self.array_cls(idx)
    with pytest.raises(ValueError, match='Lengths must match'):
        arr == arr[:1]
    with pytest.raises(ValueError, match='Lengths must match'):
        idx <= idx[[0]]