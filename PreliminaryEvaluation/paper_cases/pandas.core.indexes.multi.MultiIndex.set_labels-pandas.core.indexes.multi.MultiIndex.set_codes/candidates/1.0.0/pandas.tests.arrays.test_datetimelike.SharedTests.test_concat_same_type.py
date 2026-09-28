def test_concat_same_type(self):
    data = np.arange(10, dtype='i8') * 24 * 3600 * 10 ** 9
    idx = self.index_cls._simple_new(data, freq='D').insert(0, pd.NaT)
    arr = self.array_cls(idx)
    result = arr._concat_same_type([arr[:-1], arr[1:], arr])
    expected = idx._concat_same_dtype([idx[:-1], idx[1:], idx], None)
    tm.assert_index_equal(self.index_cls(result), expected)