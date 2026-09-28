def test_is_unique(self):
    arr = np.array(self.values, dtype=self.dtype)
    engine = self.engine_type(lambda: arr, len(arr))
    assert engine.is_unique is True
    arr = np.array(['a', 'b', 'a'], dtype=self.dtype)
    engine = self.engine_type(lambda: arr, len(arr))
    assert engine.is_unique is False