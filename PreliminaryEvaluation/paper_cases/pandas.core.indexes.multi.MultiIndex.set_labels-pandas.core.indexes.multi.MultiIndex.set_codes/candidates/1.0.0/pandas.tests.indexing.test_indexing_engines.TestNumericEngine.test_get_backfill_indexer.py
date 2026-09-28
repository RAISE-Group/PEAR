def test_get_backfill_indexer(self, numeric_indexing_engine_type_and_dtype):
    engine_type, dtype = numeric_indexing_engine_type_and_dtype
    arr = np.array([1, 5, 10], dtype=dtype)
    engine = engine_type(lambda: arr, len(arr))
    new = np.arange(12, dtype=dtype)
    result = engine.get_backfill_indexer(new)
    expected = libalgos.backfill(arr, new)
    tm.assert_numpy_array_equal(result, expected)