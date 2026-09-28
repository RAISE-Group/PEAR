def test_shift(self):
    idx = self.create_index()
    msg = 'Not supported for type {}'.format(type(idx).__name__)
    with pytest.raises(NotImplementedError, match=msg):
        idx.shift(1)
    with pytest.raises(NotImplementedError, match=msg):
        idx.shift(1, 2)