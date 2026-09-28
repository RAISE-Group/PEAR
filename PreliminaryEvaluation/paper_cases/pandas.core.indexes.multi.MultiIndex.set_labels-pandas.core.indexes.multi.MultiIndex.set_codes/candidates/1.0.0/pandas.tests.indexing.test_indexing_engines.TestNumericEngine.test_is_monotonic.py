def test_is_monotonic(self, numeric_indexing_engine_type_and_dtype):
    engine_type, dtype = numeric_indexing_engine_type_and_dtype
    num = 1000
    arr = np.array([1] * num + [2] * num + [3] * num, dtype=dtype)
    engine = engine_type(lambda: arr, len(arr))
    assert engine.is_monotonic_increasing is True
    assert engine.is_monotonic_decreasing is False
    engine = engine_type(lambda: arr[::-1], len(arr))
    assert engine.is_monotonic_increasing is False
    assert engine.is_monotonic_decreasing is True
    arr = np.array([1] * num + [2] * num + [1] * num, dtype=dtype)
    engine = engine_type(lambda: arr[::-1], len(arr))
    assert engine.is_monotonic_increasing is False
    assert engine.is_monotonic_decreasing is False