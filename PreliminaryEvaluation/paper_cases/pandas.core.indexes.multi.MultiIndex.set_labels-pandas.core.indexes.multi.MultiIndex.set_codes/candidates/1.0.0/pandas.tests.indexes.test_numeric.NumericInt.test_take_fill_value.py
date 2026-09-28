def test_take_fill_value(self):
    idx = self._holder([1, 2, 3], name='xxx')
    result = idx.take(np.array([1, 0, -1]))
    expected = self._holder([2, 1, 3], name='xxx')
    tm.assert_index_equal(result, expected)
    name = self._holder.__name__
    msg = f'Unable to fill values because {name} cannot contain NA'
    with pytest.raises(ValueError, match=msg):
        idx.take(np.array([1, 0, -1]), fill_value=True)
    result = idx.take(np.array([1, 0, -1]), allow_fill=False, fill_value=True)
    expected = self._holder([2, 1, 3], name='xxx')
    tm.assert_index_equal(result, expected)
    with pytest.raises(ValueError, match=msg):
        idx.take(np.array([1, 0, -2]), fill_value=True)
    with pytest.raises(ValueError, match=msg):
        idx.take(np.array([1, 0, -5]), fill_value=True)
    with pytest.raises(IndexError):
        idx.take(np.array([1, -5]))