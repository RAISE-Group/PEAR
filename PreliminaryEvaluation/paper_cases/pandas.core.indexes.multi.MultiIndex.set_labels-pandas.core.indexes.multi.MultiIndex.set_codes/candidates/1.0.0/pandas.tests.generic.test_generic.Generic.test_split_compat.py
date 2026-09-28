def test_split_compat(self):
    o = self._construct(shape=10)
    assert len(np.array_split(o, 5)) == 5
    assert len(np.array_split(o, 2)) == 2