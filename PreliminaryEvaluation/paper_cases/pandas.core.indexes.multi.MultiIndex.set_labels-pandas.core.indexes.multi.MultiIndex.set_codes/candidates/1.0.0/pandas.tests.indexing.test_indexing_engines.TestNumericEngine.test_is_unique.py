def test_is_unique(self, numeric_indexing_engine_type_and_dtype):
    engine_type, dtype = numeric_indexing_engine_type_and_dtype
    arr = np.array([1, 3, 2], dtype=dtype)
    engine = engine_type(lambda: arr, len(arr))
    assert engine.is_unique is True
    arr = np.array([1, 2, 1], dtype=dtype)
    engine = engine_type(lambda: arr, len(arr))
    assert engine.is_unique is False