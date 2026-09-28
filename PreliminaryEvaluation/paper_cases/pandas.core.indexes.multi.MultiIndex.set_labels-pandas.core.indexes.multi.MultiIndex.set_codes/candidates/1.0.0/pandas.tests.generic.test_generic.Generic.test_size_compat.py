def test_size_compat(self):
    o = self._construct(shape=10)
    assert o.size == np.prod(o.shape)
    assert o.size == 10 ** len(o.axes)