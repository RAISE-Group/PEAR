def test_is_monotonic(self):
    num = 1000
    arr = np.array(['a'] * num + ['a'] * num + ['c'] * num, dtype=self.dtype)
    engine = self.engine_type(lambda: arr, len(arr))
    assert engine.is_monotonic_increasing is True
    assert engine.is_monotonic_decreasing is False
    engine = self.engine_type(lambda: arr[::-1], len(arr))
    assert engine.is_monotonic_increasing is False
    assert engine.is_monotonic_decreasing is True
    arr = np.array(['a'] * num + ['b'] * num + ['a'] * num, dtype=self.dtype)
    engine = self.engine_type(lambda: arr[::-1], len(arr))
    assert engine.is_monotonic_increasing is False
    assert engine.is_monotonic_decreasing is False