def test_constructor_sanitize(self):
    s = Series(np.array([1.0, 1.0, 8.0]), dtype='i8')
    assert s.dtype == np.dtype('i8')
    s = Series(np.array([1.0, 1.0, np.nan]), copy=True, dtype='i8')
    assert s.dtype == np.dtype('f8')