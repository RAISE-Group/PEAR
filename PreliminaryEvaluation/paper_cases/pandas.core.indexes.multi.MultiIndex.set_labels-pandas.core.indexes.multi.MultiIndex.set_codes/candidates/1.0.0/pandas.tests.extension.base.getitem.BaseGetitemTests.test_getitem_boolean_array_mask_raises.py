def test_getitem_boolean_array_mask_raises(self, data):
    mask = pd.array(np.zeros(data.shape, dtype='bool'), dtype='boolean')
    mask[:2] = pd.NA
    msg = 'Cannot mask with a boolean indexer containing NA values|cannot mask with array containing NA / NaN values'
    with pytest.raises(ValueError, match=msg):
        data[mask]
    s = pd.Series(data)
    with pytest.raises(ValueError):
        s[mask]