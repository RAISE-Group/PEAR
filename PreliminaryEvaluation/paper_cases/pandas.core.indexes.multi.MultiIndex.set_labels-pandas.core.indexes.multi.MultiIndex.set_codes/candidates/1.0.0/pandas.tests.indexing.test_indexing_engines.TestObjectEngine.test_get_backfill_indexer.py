def test_get_backfill_indexer(self):
    arr = np.array(['a', 'e', 'j'], dtype=self.dtype)
    engine = self.engine_type(lambda: arr, len(arr))
    new = np.array(list('abcdefghij'), dtype=self.dtype)
    result = engine.get_backfill_indexer(new)
    expected = libalgos.backfill['object'](arr, new)
    tm.assert_numpy_array_equal(result, expected)