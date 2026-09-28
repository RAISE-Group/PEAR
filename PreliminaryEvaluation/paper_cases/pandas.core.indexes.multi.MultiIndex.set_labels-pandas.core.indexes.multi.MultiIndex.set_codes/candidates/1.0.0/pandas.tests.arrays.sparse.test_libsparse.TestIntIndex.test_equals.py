def test_equals(self):
    index = IntIndex(10, [0, 1, 2, 3, 4])
    assert index.equals(index)
    assert not index.equals(IntIndex(10, [0, 1, 2, 3]))