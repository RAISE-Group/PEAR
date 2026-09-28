def test_getitem_empty(self, data):
    result = data[[]]
    assert len(result) == 0
    assert isinstance(result, type(data))
    expected = data[np.array([], dtype='int64')]
    self.assert_extension_array_equal(result, expected)