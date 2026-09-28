def test_getitem_mask_raises(self, data):
    mask = np.array([True, False])
    with pytest.raises(IndexError):
        data[mask]
    mask = pd.array(mask, dtype='boolean')
    with pytest.raises(IndexError):
        data[mask]