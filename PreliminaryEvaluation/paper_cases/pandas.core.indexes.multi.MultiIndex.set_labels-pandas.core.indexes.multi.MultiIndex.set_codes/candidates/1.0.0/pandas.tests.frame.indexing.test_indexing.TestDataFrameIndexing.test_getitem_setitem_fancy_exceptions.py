def test_getitem_setitem_fancy_exceptions(self, float_frame):
    ix = float_frame.iloc
    with pytest.raises(IndexingError, match='Too many indexers'):
        ix[:, :, :]
    with pytest.raises(IndexingError):
        ix[:, :, :] = 1