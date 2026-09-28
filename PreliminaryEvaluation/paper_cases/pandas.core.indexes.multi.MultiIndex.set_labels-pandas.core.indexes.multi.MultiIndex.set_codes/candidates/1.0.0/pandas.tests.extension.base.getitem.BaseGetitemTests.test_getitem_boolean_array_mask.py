def test_getitem_boolean_array_mask(self, data):
    mask = pd.array(np.zeros(data.shape, dtype='bool'), dtype='boolean')
    result = data[mask]
    assert len(result) == 0
    assert isinstance(result, type(data))
    result = pd.Series(data)[mask]
    assert len(result) == 0
    assert result.dtype == data.dtype
    mask[:5] = True
    expected = data.take([0, 1, 2, 3, 4])
    result = data[mask]
    self.assert_extension_array_equal(result, expected)
    expected = pd.Series(expected)
    result = pd.Series(data)[mask]
    self.assert_series_equal(result, expected)