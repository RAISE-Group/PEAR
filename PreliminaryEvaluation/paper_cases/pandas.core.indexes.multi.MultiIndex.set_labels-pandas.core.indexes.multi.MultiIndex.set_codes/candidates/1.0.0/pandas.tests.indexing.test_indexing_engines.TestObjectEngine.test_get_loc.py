def test_get_loc(self):
    arr = np.array(self.values, dtype=self.dtype)
    engine = self.engine_type(lambda: arr, len(arr))
    assert engine.get_loc('b') == 1
    num = 1000
    arr = np.array(['a'] * num + ['b'] * num + ['c'] * num, dtype=self.dtype)
    engine = self.engine_type(lambda: arr, len(arr))
    assert engine.get_loc('b') == slice(1000, 2000)
    arr = np.array(self.values * num, dtype=self.dtype)
    engine = self.engine_type(lambda: arr, len(arr))
    expected = np.array([False, True, False] * num, dtype=bool)
    result = engine.get_loc('b')
    assert (result == expected).all()