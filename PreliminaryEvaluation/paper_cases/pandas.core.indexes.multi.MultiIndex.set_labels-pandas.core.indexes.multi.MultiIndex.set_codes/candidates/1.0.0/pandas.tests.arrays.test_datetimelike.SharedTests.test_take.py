def test_take(self):
    data = np.arange(100, dtype='i8') * 24 * 3600 * 10 ** 9
    np.random.shuffle(data)
    idx = self.index_cls._simple_new(data, freq='D')
    arr = self.array_cls(idx)
    takers = [1, 4, 94]
    result = arr.take(takers)
    expected = idx.take(takers)
    tm.assert_index_equal(self.index_cls(result), expected)
    takers = np.array([1, 4, 94])
    result = arr.take(takers)
    expected = idx.take(takers)
    tm.assert_index_equal(self.index_cls(result), expected)