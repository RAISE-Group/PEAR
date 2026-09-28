def test_get_pad_indexer(self):
    arr = np.array(['a', 'e', 'j'], dtype=self.dtype)
    engine = self.engine_type(lambda: arr, len(arr))
    new = np.array(list('abcdefghij'), dtype=self.dtype)
    result = engine.get_pad_indexer(new)
    expected = libalgos.pad['object'](arr, new)
    tm.assert_numpy_array_equal(result, expected)