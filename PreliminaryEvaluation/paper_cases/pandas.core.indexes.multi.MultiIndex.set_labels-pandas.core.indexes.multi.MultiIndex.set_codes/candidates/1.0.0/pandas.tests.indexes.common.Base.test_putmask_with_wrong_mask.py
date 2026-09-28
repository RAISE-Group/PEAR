def test_putmask_with_wrong_mask(self):
    index = self.create_index()
    with pytest.raises(ValueError):
        index.putmask(np.ones(len(index) + 1, np.bool), 1)
    with pytest.raises(ValueError):
        index.putmask(np.ones(len(index) - 1, np.bool), 1)
    with pytest.raises(ValueError):
        index.putmask('foo', 1)