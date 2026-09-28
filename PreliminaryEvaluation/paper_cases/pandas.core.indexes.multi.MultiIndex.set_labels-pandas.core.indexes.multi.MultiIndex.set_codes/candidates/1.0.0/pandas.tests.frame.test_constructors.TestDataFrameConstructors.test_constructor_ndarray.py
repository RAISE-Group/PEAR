def test_constructor_ndarray(self):
    self._check_basic_constructor(np.ones)
    frame = DataFrame(['foo', 'bar'], index=[0, 1], columns=['A'])
    assert len(frame) == 2