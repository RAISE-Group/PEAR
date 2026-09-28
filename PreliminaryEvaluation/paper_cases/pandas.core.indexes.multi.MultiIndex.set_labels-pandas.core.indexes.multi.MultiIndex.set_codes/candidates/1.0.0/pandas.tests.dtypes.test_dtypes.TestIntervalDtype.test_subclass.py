def test_subclass(self):
    a = IntervalDtype('interval[int64]')
    b = IntervalDtype('interval[int64]')
    assert issubclass(type(a), type(a))
    assert issubclass(type(a), type(b))