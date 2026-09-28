def test_get_loc(self, numeric_indexing_engine_type_and_dtype):
    engine_type, dtype = numeric_indexing_engine_type_and_dtype
    arr = np.array([1, 2, 3], dtype=dtype)
    engine = engine_type(lambda: arr, len(arr))
    assert engine.get_loc(2) == 1
    num = 1000
    arr = np.array([1] * num + [2] * num + [3] * num, dtype=dtype)
    engine = engine_type(lambda: arr, len(arr))
    assert engine.get_loc(2) == slice(1000, 2000)
    arr = np.array([1, 2, 3] * num, dtype=dtype)
    engine = engine_type(lambda: arr, len(arr))
    expected = np.array([False, True, False] * num, dtype=bool)
    result = engine.get_loc(2)
    assert (result == expected).all()